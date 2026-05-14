# Cell 1: Import libraries and download sample data
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

# Define some stocks to analyze (common financial news stocks)
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'JPM', 'BAC', 'WMT', 'PFE']

# Download 1 year of stock data
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

print(f"Downloading stock data from {start_date.date()} to {end_date.date()}")

# Download all stocks
stock_data = {}
for symbol in stocks:
    try:
        stock = yf.download(symbol, start=start_date, end=end_date)
        stock['Symbol'] = symbol
        stock_data[symbol] = stock
        print(f"Downloaded {symbol}: {len(stock)} days of data")
    except Exception as e:
        print(f"Error downloading {symbol}: {e}")

# Combine all stocks into one DataFrame
all_stocks = pd.concat(stock_data.values())
all_stocks.to_csv('data/raw/stock_prices.csv')
print(f"\nSaved {len(all_stocks)} rows to data/raw/stock_prices.csv")