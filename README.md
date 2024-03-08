Bitcoin Price Prediction Using Linear Regression

Project Overview

This project aims to predict the price of Bitcoin using historical price data. By employing linear regression, a fundamental machine learning technique, we attempt to forecast future prices based on past trends. The project demonstrates the application of data preprocessing, linear regression modeling, performance evaluation, and visualization of the results.

Limitations: 

Simple linear regression is a very basic model that assumes a linear relationship between the independent and dependent variables. If the actual relationship is not linear or if there are other influencing factors not accounted for by the model (which is likely the case with Bitcoin prices, affected by market sentiment, regulatory news, etc.), the model's predictions can be significantly off. This is seen in my Mean Squared Error (MSE) value.

The linear regression line extends slightly into negative values for money at the start. This is caused again by the volatile nature of cryptocurrencies. Having these naunce stagnations and sudden flucuations make extrapolating data increasingly difficult, making our line extend into unrealistic values. This is especially true if the slope of the regression line is negative or if the line's intercept with the Y-axis (when X=0) is negative.


Data

The dataset contains historical Bitcoin prices, including daily open, high, low, close prices, volume, and percentage change. The primary focus is on the closing price, which serves as the target variable for our predictions.

Axes: 
X axis: the days since the start of the dataset (July 18, 2010)
Y axis: The price of Bitcoin in US dollars


Methodology

Data Preprocessing
Date Conversion: Converted the 'Date' column to a datetime format to facilitate time series analysis.
Feature Engineering: Transformed the 'Date' column into a numeric format representing the number of days since the start of the dataset, used as the independent variable.
Target Variable: Utilized the 'Price' column, representing the closing price of Bitcoin, as the dependent variable.
Linear Regression Model
Implemented a simple linear regression model to predict Bitcoin prices using the transformed time feature.
Split the dataset into training (80%) and testing (20%) sets to evaluate the model's performance.
Performance Evaluation
Evaluated the model using the Mean Squared Error (MSE) and R² Score metrics to assess its accuracy and fit.
Visualization
Visualized the actual vs. predicted Bitcoin prices over time, highlighting the model's predictive capability.
Results

The linear regression model achieved an R² Score of 0.57, indicating that approximately 57% of the variance in Bitcoin prices could be explained by the model.
A plot comparing the actual and predicted prices showcases the model's effectiveness and potential areas for improvement.
Conclusion and Future Work

This project provides a foundational approach to predicting Bitcoin prices using linear regression. While the model captures a significant proportion of the variance in the data, further enhancements could improve its predictive performance. Future work may involve exploring more complex models, incorporating additional features (e.g., economic indicators, market sentiment), and applying time series analysis techniques.

How to Use

Clone the repository.
Install required Python packages: pandas, numpy, sklearn, matplotlib.
Run the Jupyter notebook or Python script to preprocess data, train the model, and visualize the results.




