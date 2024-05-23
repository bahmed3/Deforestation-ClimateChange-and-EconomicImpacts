import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

combined_data_path = r'C:\Users\notbi\OneDrive\Documents\deforestation\combined_data.csv'
combined_data = pd.read_csv(combined_data_path)

y_column = 'Tree Cover Loss (ha)'

X = combined_data[['Year']].values
y = combined_data[y_column].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

# Predict future values (next 5 years)
future_years = np.array([[2023], [2024], [2025], [2026], [2027]])
future_predictions = model.predict(future_years)

print("Predicted deforestation rates for the next 5 years:", future_predictions)

plt.figure(figsize=(10, 5))
plt.plot(combined_data['Year'], combined_data[y_column], label='Actual Tree Cover Loss', color='blue')
plt.plot(future_years, future_predictions, label='Predicted Tree Cover Loss', color='red', linestyle='dashed')
plt.xlabel('Year')
plt.ylabel('Tree Cover Loss (ha)')
plt.title('Tree Cover Loss Forecast')
plt.legend()
plt.show()
