# Import Libraries
import pandas as pd 
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl # Adjust the Size of matplotlib

# Define the start and end period

start = datetime.datetime(1995,10,16)
end = datetime.datetime(2019,12,25)

# Import prices from Yahoo Finance for S&P500

df = web.DataReader("^GSPC", 'yahoo', start, end)
df.tail()

# Plot the prices

mpl.rc('figure', figsize=(10, 10))
style.use('fast') # Check styles here: https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html
df["Adj Close"].plot(label='S&P500')
plt.legend()

# Compute the daily returns and cumulative returns

daily_returns = df["Adj Close"].pct_change()
daily_returns.tail()

# Plot Daily Returns

fig = plt.figure()
ax1 = fig.add_axes([0.5,0.5,1,1])
ax1.plot(daily_returns)
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("S&P500 daily returns data")
plt.show()

# Daily Returns Histogram

fig = plt.figure()
ax1 = fig.add_axes([0.6,0.6,1,1])
daily_returns.plot.hist(bins=80)
ax1.set_xlabel("Daily Returns %")
ax1.set_ylabel("Percent")
ax1.set_title("S&P500 Daily Returns")
ax1.text(-0.04,300,"Extreme Low\nreturns")
ax1.text(0.04,300,"Extreme High\nreturns")
plt.show()

# Cumulative Returns for S&P500

cum_returns = (daily_returns + 1).cumprod()
cum_returns.tail()

# Plot the Cumulative Returns

fig = plt.figure()
ax1 = fig.add_axes([0.5,0.5,1,1])
cum_returns.plot()
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth Rate")
ax1.set_title("S&P500 Cumulative Daily Returns")

# Mean Daily Returns

print(daily_returns.mean())

# Simple Moving Averages(SMA)

mavg30 = df["Adj Close"].rolling(window=30).mean()
mavg50 = df["Adj Close"].rolling(window=50).mean()
mavg100 = df["Adj Close"].rolling(window=100).mean()

# Print Simple Moving Averages

print(mavg30)

# Plot Simple Moving Averages

mpl.rc('figure', figsize=(10, 10))
style.use('fast')
df["Adj Close"].plot(label='S&P500')
mavg30.plot(label='mavg30')
mavg50.plot(label='mavg50')
mavg100.plot(label='mavg100')
plt.legend()

# Plot Simple Moving Averages 30 Days

mpl.rc('figure', figsize=(10, 10))
style.use('fast')
df["Adj Close"].plot(label='S&P500')
mavg30.plot(label='mavg30')
plt.legend()

# Plot Simple Moving Averages 50 Days

mpl.rc('figure',figsize=(10,10))
style.use("fast")
df["Adj Close"].plot(label='S&P500')
mavg50.plot(label='mavg50')
plt.legend()

# Plot Simple Moving Averages 100 Days

mpl.rc('figure', figsize=(10, 10))
style.use('fast')
df["Adj Close"].plot(label='S&P500', color='blue')
mavg100.plot(label='mavg100',color='red')
plt.legend()


# Exponential Moving Averages (EMA)

exp30 = df["Adj Close"].ewm(span=30, adjust=False).mean() #ewm provides exponential weighted functions.
exp50 = df["Adj Close"].ewm(span=50, adjust=False).mean()
exp100 = df["Adj Close"].ewm(span=100, adjust=False).mean()

# Plot Exponential Moving Averages

mpl.rc('figure',figsize=(10,10))
style.use("fast")
df["Adj Close"].plot(label="S&P500")
exp30.plot(label='exp30')
exp50.plot(label='exp50')
exp100.plot(label='exp100')

# Plot Exponential Moving Averages 30 Days

mpl.rc('figure',figsize=(10,10))
style.use("fast")
df["Adj Close"].plot(label="S&P500", color='blue')
exp30.plot(label='exp30', color='orange')

# Plot Exponential Moving Averages 50 Days

mpl.rc('figure',figsize=(10,10))
style.use("fast")
df["Adj Close"].plot(label="S&P500", color='blue')
exp50.plot(label='exp50', color='orange')

# Plot Exponential Moving Averages 100 Days

mpl.rc('figure',figsize=(10,10))
style.use("fast")
df["Adj Close"].plot(label="S&P500", color='blue')
exp100.plot(label='exp100', color='orange')

# Zoom on a data range using xlim

mpl.rc('figure',figsize=(10,10))
style.use("fast")
df["Adj Close"].plot(label="S&P500", color='blue')
exp100.plot(label='exp100', color='orange')
plt.xlim('2017-01-01','2019-12-25')

