import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset (adjust the file path as necessary)
file_path = r'C:\Users\Admin\Downloads\Bitcoin_history.csv' #replace this with where you've downloaded the dataset, in mycase in my downloads folder in C drive

bitcoin_data = pd.read_csv(file_path)

# Convert 'Date' to datetime format
bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'], format='%d-%b-%y')


# Clean and convert 'Price' to float
bitcoin_data['Price'] = bitcoin_data['Price'].str.replace(',', '').astype(float)

# Create 'Time' column as days from the start
bitcoin_data['Time'] = (bitcoin_data['Date'] - bitcoin_data['Date'].min()).dt.days

# Define the feature and target variable
X = bitcoin_data['Time'].values.reshape(-1, 1)  # Feature
y = bitcoin_data['Price'].values  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the testing set
y_pred = model.predict(X_test)

# Calculate and print metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='gray', label='Actual Price')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Price')
plt.title('Bitcoin Price Prediction using Linear Regression')
plt.xlabel('Time (Days)')
plt.ylabel('Price in USD')
plt.legend()
plt.show()
