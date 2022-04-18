import numpy as np
import pandas as pd

def profit(series):
    return series[-1] / series[0] - 1

def sharpe_ratio(series, risk_free=0.0, period=252):
    series = series.pct_change(1).dropna()
    ret = (1 + series.mean()) ** period - 1
    std = np.sqrt(period) * series.std(ddof=1)
    if std == 0.0:
        return np.nan
    return (ret - risk_free) / std

def calmar_ratio(series, risk_free=0.0, period=252):
    ret = series.pct_change(1).dropna()
    ret = (1 + ret.mean()) ** period - 1
    max_dd = max_drawdown(series)
    if max_dd == 0.0:
        return np.nan
    return (ret - risk_free) / abs(max_dd)

def drawdown(series):
    dd = [x / series[:i+1].max() - 1.0 for i, x in enumerate(series)]
    return pd.Series(dd, index=series.index)

def max_drawdown(series):
    dd = drawdown(series)
    return dd.min()
