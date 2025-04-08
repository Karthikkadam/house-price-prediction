import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data
data = pd.DataFrame({
    'Location': ['CityA', 'CityB', 'CityC'],
    'Size': [1000, 1500, 2000],
    'Bedrooms': [3, 4, 5],
    'Bathrooms': [2, 3, 4],
    'Floors': [1, 2, 3],
    'Year_Built': [2000, 2010, 2020],
    'House_Type': ['Apartment', 'Villa', 'Bungalow'],
    'Price': [300000, 500000, 700000]
})

# One-hot encode categorical variables
data = pd.get_dummies(data, columns=['Location', 'House_Type'])

# Separate features and target
X = data.drop('Price', axis=1)
y = data['Price']

# Train a simple model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)