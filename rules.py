import ta
import pandas as pd

class TradingRule(object):
    """This class models a systematic trading rule."""

    def __init__(self, dataset):
        self.dataset = dataset
    
    def signals(self):
        raise NotImplementedError()
    
    def _calculate(self):
        raise NotImplementedError()


class BuyAndHold(TradingRule):

    def __init__(self, dataset, **kwargs):
        super().__init__(dataset)
    
    def signals(self):
        signals = pd.Series(0, index=self.dataset.index)
        signals[0] = 1
        signals[-1] = -1
        return signals


class SMA(TradingRule):

    def __init__(self, dataset, window):
        super().__init__(dataset)
        self.window = window

    def signals(self):
        sma_series = self._calculate()
        diff = (self.dataset['Close'] - sma_series).shift(1)
        lagged_diff = diff.shift(1)
        signals = pd.Series(0, index=sma_series.index)
        signals[(diff > 0) & (lagged_diff < 0)] = 1
        signals[(diff < 0) & (lagged_diff > 0)] = -1
        return signals
    
    def _calculate(self):
        return ta.trend.sma_indicator(self.dataset['Close'], self.window)


class WMA(SMA):

    def __init__(self, dataset, window):
        super().__init__(dataset, window)
    
    def _calculate(self):
        return ta.trend.wma_indicator(self.dataset['Close'], self.window)


class EMA(SMA):

    def __init__(self, dataset, window):
        super().__init__(dataset, window)
    
    def _calculate(self):
        return ta.trend.ema_indicator(self.dataset['Close'], self.window)


class MACD(TradingRule):
    
    def __init__(self, dataset, window_slow=26, window_fast=12, window_sign=9):
        super().__init__(dataset)
        self.window_slow = window_slow
        self.window_fast = window_fast
        self.window_sign = window_sign
    
    def signals(self):
        macd_series = self._calculate()
        macd_series = macd_series.shift(1)
        lagged_macd_series = macd_series.shift(1)
        signals = pd.Series(0, index=macd_series.index)
        signals[(macd_series > 0) & (lagged_macd_series < 0)] = 1
        signals[(macd_series < 0) & (lagged_macd_series > 0)] = -1
        return signals
    
    def _calculate(self):
        return ta.trend.macd_diff(self.dataset['Close'], self.window_slow, self.window_fast, self.window_sign)


class MomentumRule(TradingRule):

    def __init__(self, dataset, window, upper_thr, lower_thr):
        super().__init__(dataset)
        self.window = window
        self.upper_thr = upper_thr
        self.lower_thr = lower_thr
    
    def signals(self):
        momentum_series = self._calculate()
        momentum_series = momentum_series.shift(1)
        lagged_momentum_series = momentum_series.shift(1)
        signals = pd.Series(0, index=momentum_series.index)
        signals[(momentum_series > self.lower_thr) & (lagged_momentum_series < self.lower_thr)] = 1
        signals[(momentum_series < self.upper_thr) & (lagged_momentum_series > self.upper_thr)] = -1
        return signals


class RSI(MomentumRule):

    def __init__(self, dataset, window, upper_thr, lower_thr):
        super().__init__(dataset, window, upper_thr, lower_thr)
        
    def _calculate(self):
        return ta.momentum.rsi(self.dataset['Close'], self.window)


class SRSI(MomentumRule):

    def __init__(self, dataset, window, upper_thr, lower_thr):
        super().__init__(dataset, window, upper_thr, lower_thr)
    
    def _calculate(self):
        return  ta.momentum.stochrsi(self.dataset['Close'], self.window) * 100.0


class SO(MomentumRule):
    def __init__(self, dataset, window, smooth_window, upper_thr, lower_thr):
        super().__init__(dataset, window, upper_thr, lower_thr)
        self.smooth_window = smooth_window
    
    def signals(self):
        k_line, d_line = self._calculate()
        k_line = k_line.shift(1)
        d_line = d_line.shift(1)
        lagged_k_line = k_line.shift(1)
        lagged_d_line = d_line.shift(1)
        signals = pd.Series(0, index=k_line.index)

        buy_condition = (k_line < self.lower_thr) & (d_line < self.lower_thr) & \
            (k_line > d_line) & (lagged_k_line < lagged_d_line)
        
        sell_condition = (k_line > self.upper_thr) & (d_line > self.upper_thr) & \
            (k_line < d_line) & (lagged_k_line > lagged_d_line)

        signals[buy_condition] = 1
        signals[sell_condition] = -1
        return signals
    
    def _calculate(self):
        k_line = ta.momentum.stoch(self.dataset['High'], self.dataset['Low'], self.dataset['Close'], self.window)
        d_line = ta.momentum.stoch_signal(self.dataset['High'], self.dataset['Low'], self.dataset['Close'], self.window, self.smooth_window)
        return k_line, d_line


class WR(MomentumRule):
    def __init__(self, dataset, window, upper_thr, lower_thr):
        super().__init__(dataset, window, upper_thr, lower_thr)
    
    def _calculate(self):
        return ta.momentum.williams_r(self.dataset['High'], self.dataset['Low'], self.dataset['Close'], self.window)