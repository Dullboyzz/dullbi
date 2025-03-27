import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Rainfall data
rainfall = [799, 1174.8, 865.1, 1334.6, 635.4, 918.5, 
            685.5, 998.6, 784.2, 985, 882.8, 1071]

# Creating a date range starting from January 2012 with monthly frequency
date_range = pd.date_range(start="2012-01", periods=len(rainfall), freq='M')

# Creating a time series DataFrame
df = pd.DataFrame({'Date': date_range, 'Rainfall': rainfall})
df.set_index('Date', inplace=True)

# Plotting the time series
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Rainfall'], marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Time Series')
plt.grid()
plt.xticks(rotation=45)

# Save the plot as PNG
plt.savefig("rainfall.png")
plt.show()
