### MAE125 Design Project Assignment 1

## Importing Modules
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

os.system('cls') # clears terminal

## CSV Reading
g_data = pd.read_csv("Geisel Data/GeiselLibrary.csv") # reads csv file
g_data_col = g_data.columns

# Day Analysis
g_data_dy = g_data[g_data['DateTime'].str.contains('11/22/2019')]

# Week Analysis
g_data_wk_1 = g_data[g_data['DateTime'].str.contains('11/16/2019')]
g_data_wk_2 = g_data[g_data['DateTime'].str.contains('11/17/2019')]
g_data_wk_3 = g_data[g_data['DateTime'].str.contains('11/18/2019')]
g_data_wk_4 = g_data[g_data['DateTime'].str.contains('11/19/2019')]
g_data_wk_5 = g_data[g_data['DateTime'].str.contains('11/20/2019')]
g_data_wk_6 = g_data[g_data['DateTime'].str.contains('11/21/2019')]
g_data_wk = pd.concat([g_data_dy, g_data_wk_6, g_data_wk_5, g_data_wk_4, g_data_wk_3, g_data_wk_2, g_data_wk_1])

# Year Analysis
g_data_yr = g_data[g_data['DateTime'].str.contains('2019')]

## Plotting
# Extracting Day Analysis Values
g_data_dy_dt = g_data_dy.DateTime
g_data_dy_rl = g_data_dy.RealPower
g_data_dy_rct = g_data_dy.ReactivePower

# Plotting Day Analysis Values
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Date & Time')
ax1.set_ylabel('Real Power [in W]', color=color)
ax1.plot(g_data_dy_dt.iloc[::-1], g_data_dy_rl, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Reactive Power [in VAR]', color=color)  # we already handled the x-label with ax1
ax2.plot(g_data_dy_dt.iloc[::-1], g_data_dy_rct, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Plot Formatting
fig.autofmt_xdate()
plt.xticks(['11/22/2019 0:00', '11/22/2019 2:00', '11/22/2019 4:00', '11/22/2019 6:00', '11/22/2019 8:00', '11/22/2019 10:00', '11/22/2019 12:00', '11/22/2019 14:00', '11/22/2019 16:00', '11/22/2019 18:00', '11/22/2019 20:00', '11/22/2019 22:00', '11/23/2019 0:00'])
fig.tight_layout()  # formats the x-axis
plt.title("Geisel Library: Real and Reactive Power Throughout A School Day")
plt.grid()
plt.show()

# Week Analysis
g_data_wk_dt = g_data_wk.DateTime
g_data_wk_rl = g_data_wk.RealPower
g_data_wk_rct = g_data_wk.ReactivePower

# Plotting Week Analysis Values
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Date & Time')
ax1.set_ylabel('Real Power [in W]', color=color)
ax1.plot(g_data_wk_dt.iloc[::-1], g_data_wk_rl, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Reactive Power [in VAR]', color=color)  # we already handled the x-label with ax1
ax2.plot(g_data_wk_dt.iloc[::-1], g_data_wk_rct, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Plot Formatting
fig.autofmt_xdate()
plt.xticks(['11/16/2019 0:00', '11/16/2019 12:00', '11/17/2019 0:00', '11/17/2019 12:00', '11/18/2019 0:00', '11/18/2019 12:00', '11/19/2019 0:00', '11/19/2019 12:00', '11/20/2019 0:00', '11/20/2019 12:00', '11/21/2019 0:00', '11/21/2019 12:00', '11/22/2019 0:00', '11/22/2019 12:00'])
fig.tight_layout()  # formats the x-axis
plt.title("Geisel Library: Real and Reactive Power Throughout A Week")
plt.grid()
plt.show()

# Year Analysis
g_data_yr_dt = g_data_yr.DateTime
g_data_yr_rl = g_data_yr.RealPower
g_data_yr_rct = g_data_yr.ReactivePower

# Plotting Year Analysis Values
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Date & Time')
ax1.set_ylabel('Real Power [in W]', color=color)
ax1.plot(g_data_yr_dt.iloc[::-1], g_data_yr_rl, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('Reactive Power [in VAR]', color=color)  # we already handled the x-label with ax1
ax2.plot(g_data_yr_dt.iloc[::-1], g_data_yr_rct, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Plot Formatting
fig.autofmt_xdate()
plt.xticks(['1/1/2019 0:00', '2/1/2019 0:00', '3/1/2019 0:00', '4/1/2019 0:00', '5/1/2019 0:00', '6/1/2019 0:00', '7/1/2019 0:00', '8/1/2019 0:00', '9/1/2019 0:00', '10/1/2019 0:00', '11/1/2019 0:00', '12/1/2019 0:00', '1/1/2020 0:00'])
fig.tight_layout()  # formats the x-axis
plt.title("Geisel Library: Real and Reactive Power Throughout A Year")
plt.grid()
plt.show()