#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('file.csv')
df = pd.read_csv('ch01.csv', index_col='Date', parse_dates=['Date'])

fig = plt.figure()
plt.plot(df.Close, '.', df.Open, '--')
fig.savefig('ch01.png')
