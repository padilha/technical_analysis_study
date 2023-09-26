import numpy as np
import pandas as pd
import math

from evaluation import sharpe_ratio
from rules import BuyAndHold

def _backtest(price_series, signals, trading_fee, initial_value=100.0):
    values = [initial_value]
    last_action = -1
    ret = price_series / price_series.shift(1)
    
    for i in range(len(price_series)):
        if i > 0:
            v = values[-1] * ret.iloc[i] if last_action == 1 else values[-1]
            values.append(v)
        
        # if i == last day of the fold
        if i == len(price_series) - 1:
            # if last action == buy, we force the strategy to sell (because the experiment will finish)
            # on the other hand, if i == last day of the fold and signals[i] == buy, we won't make
            # the operation since this is the last day of the fold and the index won't be sold afterwards
            if last_action == 1:
                values[i] *= (1 - trading_fee)
                last_action = -1
        
        # elif (last_action == sell and signals[i] == buy) or (last_action == buy and signals[i] == sell)
        elif (last_action == -1 and signals.iloc[i] == 1) or (last_action == 1 and signals.iloc[i] == -1):
            values[i] *= (1 - trading_fee)
            last_action *= -1
   
    return pd.Series(values, index=price_series.index)


class Backtest(object):
    """Backtesting class."""

    def __init__(self, dataset, trading_rule, param_grid, eval_measure,
                 first_test_year, n_years_train=5, trading_fee=0.002):
        self.dataset = dataset
        self.dataset.index = pd.to_datetime(self.dataset.index)
        self.trading_rule = trading_rule
        self.param_grid = param_grid
        self.eval_measure = eval_measure
        self.first_test_year = first_test_year
        self.n_years_train = n_years_train
        self.trading_fee = trading_fee
    
    def run(self):
        max_year = np.max(self.dataset.index.year)
        output_series = []
        fold_results = {}

        # Iterates from the first test year to the last one available.
        for test_year in range(self.first_test_year, max_year + 1):
            print(test_year, self.trading_rule)

            # Gets the training price series. Here we take one extra year in the beginning of the series
            # to be able to calculate the indicators for larger windows (ex: window=200). This extra year
            # is not used to select the best params.
            first_train_year = test_year - self.n_years_train
            dataset_train = self.dataset[(self.dataset.index.year >= first_train_year - 1) &
                                         (self.dataset.index.year < test_year)]

            param_grid = list(self.param_grid)
            if len(param_grid) == 1:
                best_params = param_grid[0]
            else:
                best_params = {}
                best_result = float('-inf')
                # p_train is the 'Close' slice from dataset_train that is used to select the best params.
                # Note that it does not include the extra year that is contained in dataset_train.
                p_train = dataset_train[dataset_train.index.year >= first_train_year]['Close']
                for params in param_grid:
                    # Creates a trading rule and gets its signals.
                    rule = self.trading_rule(dataset_train, **params)
                    signals = rule.signals()

                    # Considers only signals for dates in p_train.index.
                    s_train = signals[p_train.index]

                    # Here we discard parameters that will not perform at least a single trade during training.
                    zero_sum = (s_train == 0).sum()
                    if zero_sum < len(s_train):
                        # Runs backtest, evaluates result and check if it is the best one.
                        output = _backtest(p_train, s_train, self.trading_fee)
                        result = self.eval_measure(output)

                        if not math.isnan(result) and result > best_result:
                            best_params, best_result = params, result
                
                if len(best_params) == 0 and not (self.trading_rule == BuyAndHold):
                    raise ValueError(
                        'The input parameters do not generate any trading signal for the training '
                        f'set between {first_train_year} and {test_year-1}.'
                    )

            # Gets the test series. Note that we take one extra year, following the same idea for
            # dataset_train above.
            if self.trading_rule == BuyAndHold:
                dataset_test = self.dataset[self.dataset.index.year == test_year]
            else:
                dataset_test = self.dataset[(self.dataset.index.year == test_year - 1) |
                                            (self.dataset.index.year == test_year)]
            
            # Creates the trading rule with the best params and gets its signals.
            best_rule = self.trading_rule(dataset_test, **best_params)
            signals = best_rule.signals()
            
            # Selects only the test_year period.
            p_test = dataset_test[dataset_test.index.year == test_year]['Close']
            s_test = signals[p_test.index]

            # Runs the backtest for the test year. If this is the first test fold, then starts
            # with an initial value of 100. Otherwise, starts with the last value for the last fold
            # (to build the full series afterwards).
            if test_year == self.first_test_year:
                output_test = _backtest(p_test, s_test, self.trading_fee, initial_value=100.0)
            else:
                output_test = _backtest(p_test, s_test, self.trading_fee, initial_value=output_series[-1][-1])
            
            fold_results[test_year] = self.eval_measure(output_test)
            output_series.append(output_test)

        # Concatenates the resulting series into a single one and returns it.
        output_series = pd.concat(output_series)
        return output_series, fold_results
