### MAE125 Design Project Assignment 1

## Importing Modules
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

os.system('cls') # clears terminal

## CSV Reading
g_data = pd.read_csv("GeiselLibrary.csv") # reads csv file
g_data_col = g_data.columns

# Day Analysis
g_data_dy = g_data[g_data['DateTime'].str.contains('12/31/2019')]

# Week Analysis
g_data_wk_1 = g_data[g_data['DateTime'].str.contains('12/25/2019')]
g_data_wk_2 = g_data[g_data['DateTime'].str.contains('12/26/2019')]
g_data_wk_3 = g_data[g_data['DateTime'].str.contains('12/27/2019')]
g_data_wk_4 = g_data[g_data['DateTime'].str.contains('12/28/2019')]
g_data_wk_5 = g_data[g_data['DateTime'].str.contains('12/29/2019')]
g_data_wk_6 = g_data[g_data['DateTime'].str.contains('12/30/2019')]
g_data_wk = pd.concat([g_data_dy, g_data_wk_6, g_data_wk_5, g_data_wk_4, g_data_wk_3, g_data_wk_2, g_data_wk_1])

# Annual Analysis
g_data_yr = g_data[g_data['DateTime'].str.contains('2019')]

## Plotting
# Day Analysis
g_data_dy_dt = g_data_dy.DateTime
g_data_dy_rl = g_data_dy.RealPower
g_data_dy_rct = g_data_dy.ReactivePower

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date & Time')
ax1.set_ylabel('Real Power', color=color)
ax1.plot(g_data_dy_dt.iloc[::-1], g_data_dy_rl, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Reactive Power', color=color)  # we already handled the x-label with ax1
ax2.plot(g_data_dy_dt.iloc[::-1], g_data_dy_rct, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.autofmt_xdate()
plt.xticks(["12/31/2019 0:00", "12/31/2019 2:00", "12/31/2019 4:00", "12/31/2019 6:00", "12/31/2019 8:00", "12/31/2019 10:00", "12/31/2019 12:00", "12/31/2019 14:00", "12/31/2019 16:00", "12/31/2019 18:00", "12/31/2019 20:00", "12/31/2019 22:00"])
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

# Day Analysis
g_data_wk_dt = g_data_wk.DateTime
g_data_wk_rl = g_data_wk.RealPower
g_data_wk_rct = g_data_wk.ReactivePower

# Day Analysis
g_data_yr_dt = g_data_yr.DateTime
g_data_yr_rl = g_data_yr.RealPower
g_data_yr_rct = g_data_yr.ReactivePower