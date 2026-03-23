P9: Time Series Analysis



sales <- c(120,130,150,170,160,180,200,220,210,230,250,270,125,135,155,175,165,185,205,225,215,235,255,275)



ts\_data <- ts(sales, start = c(2023, 1), frequency = 12)



print(ts\_data)



plot(ts\_data, main="Monthly Sales", col="blue", ylab="Sales", xlab="Time")



decomp <- decompose(ts\_data, type="additive")

plot(decomp)



ma <- filter(ts\_data, rep(1/3,3), sides=2)

plot(ts\_data, col="blue")

lines(ma, col="red")



install.packages("tseries")

library(tseries)



adf.test(ts\_data)



install.packages("forecast")

library(forecast)



auto.arima(ts\_data)



model <- auto.arima(ts\_data)

summary(model)



future <- forecast(model, h=6)

plot(future)



accuracy(future)





**What is Time Series Analysis?**

Time Series Analysis is a statistical technique used to analyze data points collected or recorded at specific time intervals. It helps identify trends, seasonality, and patterns to make forecasts.



**Step 1: Create Time Series Dataset**

* ts\_data <- ts(sales, start = c(2023, 1), frequency = 12)

Converts sales data into a time series object.

start = c(2023,1) → starts from January 2023.

frequency = 12 → monthly data.



**Step 2: Plot Time Series**

* plot(ts\_data, main="Monthly Sales", col="blue", ylab="Sales", xlab="Time")

Plots sales data over time.

Helps visualize trends and fluctuations.



**Step 3: Decomposition**

* decomp <- decompose(ts\_data, type="additive")
* plot(decomp)

Breaks time series into Trend, Seasonality, and Random components.

Useful for understanding underlying patterns.



**Step 4: Moving Average**

* ma <- filter(ts\_data, rep(1/3,3), sides=2)
* plot(ts\_data, col="blue")
* lines(ma, col="red")

Smooths data using a moving average.

Red line shows smoothed trend.



**Step 5: Stationarity Test**

* adf.test(ts\_data)

Augmented Dickey-Fuller (ADF) test checks if the series is stationary (constant mean/variance over time).

Stationarity is required for ARIMA modeling.



**Step 6: ARIMA Model**

* model <- auto.arima(ts\_data)
* summary(model)

Fits the best ARIMA model automatically.

ARIMA = AutoRegressive Integrated Moving Average.

Summary shows coefficients and model fit.



**Step 7: Forecast Future Values**

* future <- forecast(model, h=6)
* plot(future)
* accuracy(future)

Forecasts next 6 months of sales.

Plot shows predicted values with confidence intervals.

accuracy() gives error metrics (MAE, RMSE, etc.).



**Summary**

Time Series Analysis helps in forecasting future values based on past data.

This practical demonstrates:

* Creating time series data
* Visualizing trends
* Decomposition
* Moving averages
* Stationarity testing
* ARIMA modeling
* Forecasting future sales

