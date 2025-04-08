# Bangalore Real Estate Data Analysis

This project contains a dataset of real estate properties in Bangalore, India. The dataset includes various property listings with detailed information about their features, locations, and pricing.

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

## Usage

This dataset can be used for:
- Real estate market analysis
- Property price prediction
- Location-based property value assessment
- Market trend analysis

## Requirements

To work with this dataset, you'll need:
- Python 3.x
- Pandas
- NumPy
- Matplotlib/Seaborn (for visualization)

## Getting Started

1. Clone this repository
2. Install required dependencies
3. Load the dataset using pandas:
   ```python
   import pandas as pd
   df = pd.read_csv('data.csv')
   ```

## License

This dataset is provided for educational and research purposes. 