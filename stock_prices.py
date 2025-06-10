import yfinance as yfin

#Ticker symbols
ticker_symbol1 = "AAPL"

#Creating a ticker object
ticker1 = yfin.Ticker(ticker_symbol1)

#Fetching historicaal market data
history_data = ticker1.history(period = "6mo") #data for past 5 years
print("historical data:")
print(history_data)

#Fetching basic financials
financials = ticker1.financials
print("\nFinancials:")
print(financials)

#Fetching info about dividends and splits
dividends = ticker1.dividends
print("\nDividends:")
print(dividends)
splits = ticker1.splits
print("\nSplits:")
print(splits)






