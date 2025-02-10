# Forecasting Using Python

# Shampoo Sales Forecasting using Exponential Smoothing & Prophet

## Project Description
This repository contains a Python-based forecasting model for predicting shampoo sales using both the Exponential Smoothing and Prophet methods. The model uses historical monthly sales data to forecast future sales for the next 12 months.

The code implements key steps such as testing for stationarity using the Augmented Dickey-Fuller test, differencing to make the data stationary if necessary, and then using two forecasting models:
1. Holt-Winters Exponential Smoothing for capturing seasonality and trend.
2. Prophet model by Facebook for time series forecasting, which also handles missing data and outliers.

## Steps followed.
1. **Installation**: 
Clone the repository:

```bash
git clone https://github.com/yourusername/Shampoo-Sales-Forecast.git
````
````bash
cd Shampoo-Sales-Forecast
````

2. **Install required libraries**:

```bash
pip install -r requirements.txt
````
3. **Usage**
Download the dataset shampoo-sales.csv (or use your own sales data in CSV format).
Place the CSV file in the same directory as the Python script.
Run the Python script to train the model and generate forecasts:

```bash
python forecast_shampoo_sales.py
````

## This script will:

- Load and process the data from the CSV file.
- Perform a stationarity test (ADF test) and differencing if necessary.
- Apply both the Exponential Smoothing and Prophet models.
- Forecast the next 12 months of shampoo sales.
- Plot the actual sales and the forecasted values from both models.
- Compare the forecasts from Exponential Smoothing (Holt-Winters) and Prophet.

## Input Data
- The dataset should be a CSV file with the following columns:

- Month: The month of the sales data (should be in a recognizable date format such as YYYY-MM).
- Sales: The sales figures for the corresponding month.
- Example (shampoo-sales.csv):

## csv
````bash
Month,Sales
2001-01,150
2001-02,160
2001-03,170
...
````

## Model Details

### Exponential Smoothing (Holt-Winters)

The forecasting model uses Exponential Smoothing (specifically the Holt-Winters method), which is suitable for time series data that exhibit both trend and seasonality. The model components include:

- Trend: Added to the forecast to capture the general upward or downward movement.
- Seasonality: Captures periodic fluctuations in the data (12 periods for monthly data).
- The model is fit using historical sales data and generates a forecast for the next 12 months.

### Prophet Model

The Prophet model by Facebook is designed for forecasting time series data with strong seasonality and potential holiday effects. Prophet automatically handles missing data, outliers, and seasonal patterns, and allows for easy tuning.

- Seasonality: Prophet can model yearly, weekly, and daily seasonality.
- Trends: Captures long-term trends in the data.
- Holidays: It also supports the addition of special events (holidays) if they are relevant.
Once the Prophet model is trained, it will predict future sales for the next 12 months, and the results will be compared with the Exponential Smoothing method.

## Forecasting
Once both models are fitted, they predict future values (next 12 months in this case) and plots both the actual sales and forecasted values on a graph.

The forecast is shown in a red dashed line, and the actual sales are plotted as blue markers.

- Dependencies
- pandas
- numpy
- statsmodels
- matplotlib
  
## You can install these dependencies by running:

````bash
pip install -r requirements.txt
````

## Screenshots

Here is a screenshot of the Exponential Smoothing Forecast Model:
![Exponential Smoothing Forecast Model Screenshot](https://github.com/Sakushal/Python-Forecasting-Model/blob/main/Exponential_Smoothing_Forecast/Exponential%20Smoothing%20img.png)

Here is a screenshot of the Prophet Forecast Model:
![Prophet Forecast Model Screenshot](https://github.com/Sakushal/Python-Forecasting-Model/blob/main/Prophet_Forecast/Prophet%20img.png)


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request.

## Contact Information
For any questions or issues, feel free to reach out at saksalstha@gmail.com.
