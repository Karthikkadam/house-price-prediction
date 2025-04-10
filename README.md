# Bangalore Real Estate Data Analysis and Price Prediction

This project contains a dataset of real estate properties in Bangalore, India, and a web application for predicting house prices based on various features. The dataset includes various property listings with detailed information about their features, locations, and pricing.

## Dataset Description

The dataset (`data.csv`) contains information about properties with the following attributes:

- **Area Type**: Type of property area (Super built-up Area, Built-up Area, Plot Area)
- **Availability**: Ready to move status or possession date
- **Location**: Area/neighborhood in Bangalore
- **Size**: Number of BHKs or bedrooms
- **Society**: Name of the housing society (if applicable)
- **Total Area**: Total area in square feet
- **Bathrooms**: Number of bathrooms
- **Balconies**: Number of balconies
- **Price**: Property price in lakhs (1 lakh = 100,000 INR)

## Data Fields

1. `area_type`: Type of property area
2. `availability`: Possession status or date
3. `location`: Property location
4. `size`: Number of BHKs/bedrooms
5. `society`: Housing society name
6. `total_sqft`: Total area in square feet
7. `bath`: Number of bathrooms
8. `balcony`: Number of balconies
9. `price`: Price in lakhs

## Web Application

The project includes a Flask web application that allows users to predict house prices based on the property features. The application provides a user-friendly interface with dropdown menus populated from the actual dataset.

### Features
- Interactive web interface for entering property details
- Dropdown menus for all categorical fields with real values from the dataset
- Real-time price prediction using a trained machine learning model
- Responsive design for desktop and mobile devices

## Project Components

1. `data.csv` - Dataset containing real estate information
2. `train_model.py` - Script to train the machine learning model
3. `model.pkl` - Trained machine learning model (saved using pickle)
4. `app.py` - Flask application for serving the web interface
5. `templates/index.html` - HTML template for the web interface

## Requirements

To run this project, you'll need:
- Python 3.x
- Flask
- Pandas
- NumPy
- Scikit-learn
- Pickle

Install dependencies:
```
pip install flask pandas numpy scikit-learn
```

## Getting Started

1. Clone this repository
2. Install required dependencies
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open a web browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. Select property details from the dropdown menus
2. Enter the total square footage, number of bathrooms, and balconies
3. Click "Predict Price" to get an estimated property value

## Model Training

The machine learning model was trained using the `train_model.py` script:
1. The data is loaded and preprocessed
2. Categorical variables are converted using one-hot encoding
3. A Linear Regression model is trained
4. The model is saved as `model.pkl` for use in the web application

## License

This dataset and application are provided for educational and research purposes. 