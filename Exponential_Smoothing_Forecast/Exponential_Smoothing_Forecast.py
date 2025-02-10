import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# from statsmodels.tsa.arima.model import ARIMA
# from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Load the CSV file
data = pd.read_csv("D:\Shampoo Sales Forecast\Exponential_Smoothing_Forecast\shampoo-sales.csv")

# Display the first few rows
#print(data.head())

data['Month'] = pd.date_range(start='2001-01',periods=len(data), freq='M')
data.set_index('Month', inplace=True)

result = adfuller(data['Sales'])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

# Output the results
if result[1] > 0.05:
    print('The data is non-stationary.')    
else:
    print('The data is stationary.')
    
data_diff = data.diff().dropna()

result_diff = adfuller(data_diff['Sales'])
print('ADF Statistic: %f' % result_diff[0])
print('p-value: %f' % result_diff[1])


# Output the results
if result_diff[1] > 0.05:
    print('The data is non-stationary.')    
else:
    print('The data is stationary.')
   
   
 # Plot the ACF and PACF plots

# plt.figure(figsize=(10,5))
# plot_acf(data_diff, lags=18)
# plt.show()

# plt.figure(figsize=(10,5))
# plot_pacf(data_diff, lags=18)
# plt.show()   
     
  
  # Fit Holt-Winters seasonal model (trend='add', seasonal='add', period=12 for monthly data)
model_hw = ExponentialSmoothing(data, trend='add', seasonal='add', seasonal_periods=12)
model_hw_fit = model_hw.fit()

# Forecasting next 12 months
Forecast = model_hw_fit.forecast(steps=12)

  # Generate future dates for plotting
future_dates = pd.date_range(start=data.index[-1], periods=13, freq="M")[1:]

  # Plot results
plt.figure(figsize=(10, 5))
plt.plot(data, label="Actual Sales", marker="o")
plt.plot(future_dates, Forecast, label="Forecast", color='red', linestyle="dashed", marker="o")
plt.legend()
plt.title("Shampoo Sales Forecast")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
