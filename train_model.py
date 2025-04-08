import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("data.csv")

# Function to convert sqft ranges to numeric
def convert_sqft_to_num(sqft):
    try:
        if "-" in sqft:
            vals = list(map(float, sqft.split('-')))
            return np.mean(vals)
        return float(sqft)
    except:
        return None

# Apply conversion
df["total_sqft"] = df["total_sqft"].astype(str).apply(convert_sqft_to_num)

# Drop or fill NaN values
df.dropna(inplace=True)  # Drop rows with missing values (Recommended)
# df.fillna(df.mean(), inplace=True)  # Alternative: Fill with mean

# Feature selection
X = df.drop(["price"], axis=1)
y = df["price"]

# Convert categorical variables
X = pd.get_dummies(X)

# Drop NaNs in X after encoding
X.dropna(inplace=True)
y = y[X.index]  # Align y with X

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
