import yfinance as yfin
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import mplcursors

#Fetching historicaal market data
history_data = yfin.download("AAPL", start="2020-01-01", end="2025-05-01", interval="1d")

print("historical data:")
print(history_data)

#Simple Moving Average (SMA) 20-day calculation 
history_data['SMA'] = history_data['Close'].rolling(window=20).mean()  # 20-day Simple Moving Average
print(history_data["SMA"].tail(100))

APPLE = history_data['SMA']
fig, ax = plt.subplots()
line, = ax.plot(history_data.index, APPLE, label='AAPL', color='blue', linewidth=2)  # Capture line and use fig/ax
plt.legend(loc='upper left')
plt.title("20 day Simple Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
cursor = mplcursors.cursor(line, hover=True) #Cursor for interactive data point display

plt.show()












