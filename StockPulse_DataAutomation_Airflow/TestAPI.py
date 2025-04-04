import yfinance as yf

tickers = ["AAPL", "MSFT"]
start_date = "2018-01-01"
end_date = "2024-01-01"

try:
    data = yf.download(tickers, start=start_date, end=end_date)
    if data.empty:
        print("No data retrieved.")
    else:
        print(data)  # Print the data to see if it works
except Exception as e:
    print(f"Error: {e}")