import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import matplotlib.ticker as mticker

# Load the CSV file
data = pd.read_csv("D:\Shampoo Sales Forecast\Prophet_Forcast\shampoo-sales.csv")

# Convert 'Month' to datetime format - uncomment and modify this line
data['Month'] = pd.to_datetime(data['Month'])  # Remove the format parameter if your dates are already in standard format

# Rename columns to match Prophet's requirements
data = data.rename(columns={'Month': 'ds', 'Sales': 'y'})

# Initialize and fit the Prophet model
model = Prophet(seasonality_mode='additive', yearly_seasonality=True)
model.fit(data)

# Create a future dataframe for the next 20 months
future = model.make_future_dataframe(periods=20, freq='M')

# Generate the forecast
forecast = model.predict(future)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(data['ds'], data['y'], label="Actual Sales", marker="o")
plt.plot(forecast['ds'], forecast['yhat'], label="Forecast", color='red', linestyle="dashed", marker="o")
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.3)  # Confidence interval

# Format the y-axis to show actual values
ax = plt.gca()
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x:,.0f}'))  # Format with commas

plt.legend()
plt.title("Shampoo Sales Forecast Using Prophet")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# # Show the dataframe in a scrollable GUI
# show(merged_data)