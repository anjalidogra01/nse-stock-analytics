import yfinance as yf
import pandas as pd

tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS", 
           "HDFCBANK.NS", "WIPRO.NS",
           "BAJFINANCE.NS", "SUNPHARMA.NS", "MARUTI.NS", "ADANIENT.NS"]

print("Fetching data from Yahoo Finance...")

all_data = []

for ticker in tickers:
    df = yf.download(ticker, start="2020-01-01", end="2025-12-30", 
                     progress=False, auto_adjust=True)
    df.columns = df.columns.get_level_values(0)  # flatten multi-level columns
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df["Ticker"] = ticker
    df = df.reset_index()
    df.rename(columns={"Date": "Date"}, inplace=True)
    all_data.append(df)

final_df = pd.concat(all_data, ignore_index=True)
final_df.rename(columns={"index": "Date"}, inplace=True)
final_df.to_csv("raw_stock_data.csv", index=False)

print(f"Data Extracted successfully!")
print(f"Total rows: {len(final_df)}")
print(final_df[["Date", "Ticker", "Open", "Close", "Volume"]].head())