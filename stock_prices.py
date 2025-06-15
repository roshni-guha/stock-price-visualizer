import yfinance as yfin
import matplotlib.pyplot as plt
import matplotlib.animation
import mplcursors
import subprocess

subprocess.Popen(["python3", "data_GUI.py"]) #Running this and GUI simultaneously

#Fetching historicaal market data
history_data_AAPL = yfin.download("AAPL", start="2020-01-01", end="2025-05-01", interval="1d")
history_data_MSFT = yfin.download("MSFT", start="2020-01-01", end="2025-05-01", interval="1d")

print("historical data of Apple:")
print(history_data_AAPL)
print("historical data of Microsoft:")
print(history_data_MSFT)

#Simple Moving Average (SMA) 20-day calculation 
history_data_AAPL['SMA'] = history_data_AAPL['Close'].rolling(window=20).mean()  # 20-day Simple Moving Average of Apple
history_data_MSFT['SMA'] = history_data_MSFT['Close'].rolling(window=20).mean()  # 20-day Simple Moving Average of Microsoft
print(history_data_AAPL["SMA"].tail(100))
print(history_data_MSFT["SMA"].tail(100))

APPLE = history_data_AAPL['SMA']
MSFT = history_data_MSFT['SMA']
fig, ax = plt.subplots()
line, = ax.plot(history_data_AAPL.index, APPLE, label='AAPL', color='blue', linewidth=2)  # Capture line and use fig/ax

plt.title("20 day Simple Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
cursor = mplcursors.cursor(line, hover=False) #Cursor for interactive data point display


line2, = ax.plot(history_data_MSFT.index, MSFT, label='MSFT', color='orange', linewidth=2)  # Capture line2
cursor2 = mplcursors.cursor(line2, hover=False)  # Cursor for interactive data point display

plt.legend(loc='upper left')
plt.show()








