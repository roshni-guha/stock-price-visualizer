import tkinter as tk
import yfinance as yfin

# Download historical data
data_aapl = yfin.download("AAPL", start="2020-01-01", end="2025-05-01").dropna()
data_msft = yfin.download("MSFT", start="2020-01-01", end="2025-05-01").dropna()

# Convert to plain strings
text_aapl = data_aapl.to_string()
text_msft = data_msft.to_string()

# Create main window
root = tk.Tk()
root.title("AAPL and MSFT Historical Data")
root.geometry("1000x600") #Size of the window
root.resizable(True, True)  # Allow resizing of the window
root.configure(bg='lightblue')  # Set background color of the window

# Left frame for AAPL
frame_aapl = tk.Frame(root) #Frame for AAPL data
frame_aapl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #Position the frame on the left side of the window

scrollbar_aapl = tk.Scrollbar(frame_aapl)
scrollbar_aapl.pack(side=tk.RIGHT, fill=tk.Y) # Scrollbar for AAPL data

text_widget_aapl = tk.Text(frame_aapl, wrap=tk.NONE, yscrollcommand=scrollbar_aapl.set) # Text widget for AAPL data
text_widget_aapl.insert(tk.END, text_aapl)
text_widget_aapl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_aapl.config(command=text_widget_aapl.yview)

# Right frame for MSFT
frame_msft = tk.Frame(root) #Frame for MSFT data
frame_msft.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) #Position the frame on the right side of the window

scrollbar_msft = tk.Scrollbar(frame_msft)
scrollbar_msft.pack(side=tk.RIGHT, fill=tk.Y) # Scrollbar for MSFT data

text_widget_msft = tk.Text(frame_msft, wrap=tk.NONE, yscrollcommand=scrollbar_msft.set)
text_widget_msft.insert(tk.END, text_msft)
text_widget_msft.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_msft.config(command=text_widget_msft.yview)

root.mainloop() 
