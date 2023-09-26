## Trend and Momentum Indicators for Investing in Market Indices

This repository contains the codes for the experiments from the paper _Trend and Momentum Indicators for Investing in Market Indices_.

__Summary:__
* [Abstract](#abstract)
* [How to install and run](#how-to-install-and-run)
* [File description](#file-description)
* [License (MIT)](LICENSE.txt)

### Abstract

Technical analysis indicators use only past prices and volumes of shares traded to determine when to buy or sell a security. Its effectivity has been the subject of study for decades in the economics literature. Many favorable and unfavorable papers have already been published. Considering such a debate, we introduced an empirical study of 4 trend indicators and 4 momentum indicators for the investment on 7 different market indices. Additionally, we employed a parameter optimization methodology for each indicator, and compared their results with those achieved by classical parameters reported in the literature. For the evaluation of each indicator, we used two risk-adjusted performance measures. Afterwards, the best results of each indicator were compared with the passive buy-and-hold strategy, which consists of buying a security and keeping it for a long period before selling it. During the experiments, we have not identified any improvements in the results that justify the extra computational step required by the optimization procedure. Besides, no technical indicator was able to consistently beat the buy-and-hold strategy in the long run.

### How to install and run

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

2. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) on your system (as an alternative, you can [install git using conda](https://anaconda.org/anaconda/git)).

3. Open a terminal and clone this repository.

```
git clone https://github.com/padilha/technical_analysis_study.git
```

4. Create and activate conda environment.

```
conda env create -f env.yml -n ta-study
conda activate ta-study
```

5. Fetch the datasets from Yahoo Finance:

```
python data.py
```

6. To list the available command line arguments type:

```
python experiment.py -h
```

The available options are:

* ```-h``` : displays the help message.

* ```-d``` : datasets directory.

* ```-o``` : output directory.

* ```-n``` : number of jobs to run in parallel (default: 1).

* ```-r``` : risk-free file path (default: ```./US_TBond.csv```).

7. Example of how to run:

```
python experiment.py -d ./datasets -o ./output -n 5
```

8. After running the codes, you can deactivate the environment.

```
conda deactivate
```

### File description

* ```US_TBond.csv``` : annual returns on investiments in US T. Bond (source: [Damodaran](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html)). It is used as the risk-free rate for the Sharpe ratio.

* ```backtest.py``` : backtesting structure. It performs parameter optimization of the trading rules and simulates trades and fees.

* ```data.py``` : fetches price and volume series from Yahoo Finance.

* ```env.yml``` : specifies the virtual environment for this project.

* ```evaluation.py``` : evaluation measures (Sharpe ratio and Calmar ratio).

* ```experiment.py``` : runs the experiment.

* ```rules.py``` : contains the implementation of trading rules.

* ```results_default.zip```: result files of the default parameters.

* ```results_optimization.zip```: result files of the parameter optimization procedure.

* Each result filename follows the convention MARKET__STRATEGY__EVALUATIONMEASURE (for example DJIA__BH__calmar refers to the results of the buy-and-hold strategy on the Dow Jones Industry Average Index using the Calmar ratio). For each market-strategy-evaluation combination, there are two files:
    * JSON file: contains the dictionary of results in the format {year : evaluation measure value}.

    * CSV file: contains the resulting time series.
