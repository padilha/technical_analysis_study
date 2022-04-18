import pandas as pd
import yfinance as yf
import os

NAMES = {
    '^GSPC'     : 'S&P 500',       # Standard & Poor's 500 (USA)
    '^DJI'      : 'DJIA',          # Dow Jones Industrial Average (USA)
    '^IXIC'     : 'NASDAQ',        # NASDAQ Composite (USA)
    '^N100'     : 'Euronext 100',  # Euronext 100 blue chip index of the pan-European exchange (Europe)
    '^HSI'      : 'HSI',           # Hang Seng Index (Hong Kong)
    '000001.SS' : 'SSE Composite', # Shangai Stock Exchange Composite (China)
    '^BVSP'     : 'IBOVESPA',      # Sao Paulo Stock Exchange Index (Brazil)
}

tickers = NAMES.keys()
output_dir = 'datasets'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for t in tickers:
    print(t)
    df = yf.download(t, start='1922-01-01', end='2021-12-31')
    name = NAMES[t]
    df.to_csv(output_dir + '/' + name + '.csv')
