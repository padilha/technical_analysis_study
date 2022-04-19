import sys
import os
import re
import json
import pandas as pd
import multiprocessing as mp
import marshal
import types

from sklearn.model_selection import ParameterGrid
from rules import SMA, RSI, EMA, WMA, MACD, RSI, SRSI, SO, WR, BuyAndHold
from evaluation import sharpe_ratio, calmar_ratio
from backtest import Backtest

TRADING_RULES = {
    'SMA' : (SMA, ParameterGrid({'window' : [10, 15, 20, 25, 30, 50, 65, 80, 130, 200]})),
    'SMA' : (SMA, ParameterGrid({'window' : [10, 15, 20, 25, 30, 50, 65, 80, 130, 200]})),
    'WMA' : (WMA, ParameterGrid({'window' : [10, 15, 20, 25, 30, 50, 65, 80, 130, 200]})),
    'EMA' : (EMA, ParameterGrid({'window' : [10, 15, 20, 25, 30, 50, 65, 80, 130, 200]})),

    'MACD' : (MACD, ParameterGrid({'window_slow' : [10, 15, 20, 25, 30],
                                   'window_fast' : [50, 65, 80, 130, 200],
                                   'window_sign' : [6, 9, 12]})),

    'RSI' : (RSI, ParameterGrid({'window'    : [5, 7, 9, 14, 21, 25, 28, 30, 45],
                                 'upper_thr' : [60, 65, 70, 75, 80],
                                 'lower_thr' : [20, 25, 30, 35, 40]})),
    
    'SRSI' : (SRSI, ParameterGrid({'window'    : [5, 7, 9, 14, 21, 25, 28, 30, 45],
                                   'upper_thr' : [60, 65, 70, 75, 80],
                                   'lower_thr' : [20, 25, 30, 35, 40]})),
    
    'SO' : (SO, ParameterGrid({'window'    : [5, 7, 9, 14, 21, 25, 28, 30, 45],
                               'smooth_window' : [3, 6, 9],
                               'upper_thr' : [60, 65, 70, 75, 80],
                               'lower_thr' : [20, 25, 30, 35, 40]})),

    'WR' : (WR, ParameterGrid({'window'    : [5, 7, 9, 14, 21, 25, 28, 30, 45],
                               'lower_thr' : [-60, -65, -70, -75, -80],
                               'upper_thr' : [-20, -25, -30, -35, -40]})),

    'BH' : (BuyAndHold, {})
}

EVALUATION_MEASURES = {
    'sharpe' : sharpe_ratio,
    'calmar' : calmar_ratio
}

FIRST_TEST_YEAR = {
    'DJIA' : 1998,
    'Euronext 100' : 2006,
    'HSI' : 1993,
    'IBOVESPA' : 2000,
    'NASDAQ' : 1978,
    'S&P 500' : 1934,
    'SSE Composite' : 2004
}

def run_experiment(backtest, output_dir, dataset_name, rule_name, eval_measure_name, risk_free):
    if eval_measure_name == 'sharpe':
        first_year = backtest.first_test_year
        last_year = backtest.dataset.index.year.max()
        interval = risk_free.loc[first_year:last_year]
        n_years = len(interval)
        risk_free_rate = ((1 + interval).prod()) ** (1.0 / n_years) - 1
        backtest.eval_measure = lambda s : sharpe_ratio(s, risk_free=risk_free_rate)
    
    output_series, fold_results = backtest.run()
    dataset_name = re.sub('\s+', '_', dataset_name)
    out_prefix = f'{output_dir}/{dataset_name}__{rule_name}__{eval_measure_name}'
    output_series.to_csv(out_prefix + '.csv')
    
    with open(out_prefix + '.json', 'w') as file_:
        json.dump(fold_results, file_)

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-d', '--datasets-directory', dest='data_dir', type=str)
    parser.add_argument('-o', '--output-directory', dest='output_dir', type=str)
    parser.add_argument('-n', '--number-of-jobs', dest='n_jobs', type=int, default=1)
    parser.add_argument('-r', '--risk-free-file', dest='risk_free_file', type=str, default='./US_TBond.csv')
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    
    files = os.listdir(args.data_dir)
    datasets = {}
    for f in files:
        name = f.split('.')[0]
        datasets[name] = pd.read_csv(f'{args.data_dir}/{f}', header=0, index_col=0).fillna(method='ffill')
    
    risk_free = pd.read_csv(args.risk_free_file, header=0, index_col=0)
    risk_free = risk_free[risk_free.columns[0]]

    pool = mp.Pool(processes=args.n_jobs)
    for r_name, (constructor, grid) in TRADING_RULES.items():
        params = []
        for d_name, dataset in datasets.items():
            for e_name in EVALUATION_MEASURES:
                eval_measure = EVALUATION_MEASURES[e_name]
                b = Backtest(dataset, constructor, grid, eval_measure, FIRST_TEST_YEAR[d_name])
                params.append((b, args.output_dir, d_name, r_name, e_name, risk_free))
        
        pool.starmap(run_experiment, params)

    pool.close()
    pool.join()
