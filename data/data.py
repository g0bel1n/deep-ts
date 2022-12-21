#%%

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from finta import TA 


sns.set()

#%%

df = pd.read_csv("data/IVE_bidask1min.txt", sep=',', infer_date_format=True)


# %%
df.plot(y="Adj Close")
# %%
TA.EMA(df, 20).plot()
# %%


df['ema'] = TA.EMA(df, 20)
df['rsi'] = TA.RSI(df)
df['macd'] = TA.MACD(df).MACD
df['macd_signal'] = TA.MACD(df).SIGNAL

# %%

df.plot(y=['rsi', 'macd', 'macd_signal'])
# %%

df.dropna(inplace=True)

# %%
df.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume'], inplace=True)
# %%
df.to_csv('data/SPY.csv')
# %%
