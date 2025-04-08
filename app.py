from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load the CSV data
data = pd.read_csv('data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    area_type = request.form['area_type']
    availability = request.form['availability']
    location = request.form['location']
    size = request.form['size']
    society = request.form['society']
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    # Create DataFrame for input
    input_data = pd.DataFrame([[area_type, availability, location, size, society, total_sqft, bath, balcony]],
                              columns=['area_type', 'availability', 'location', 'size', 'society', 'total_sqft', 'bath', 'balcony'])

    # One-hot encoding
    input_data = pd.get_dummies(input_data, columns=['area_type', 'availability', 'location', 'size', 'society'])

    # Ensure columns match training data
    model_columns = model.feature_names_in_
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    # Predict price
    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction_text=f'Estimated House Price: ₹{prediction:.2f}')


@app.route('/suggestions', methods=['GET'])
def suggestions():
    query = request.args.get('query', '')
    suggestions = {
        'area_type': data['area_type'].dropna().unique().tolist(),
        'availability': data['availability'].dropna().unique().tolist(),
        'location': data['location'].dropna().unique().tolist(),
        'size': data['size'].dropna().unique().tolist(),
        'society': data['society'].dropna().unique().tolist()
    }
    filtered_suggestions = {key: [s for s in values if query.lower() in s.lower()][:3] for key, values in suggestions.items()}
    return jsonify(filtered_suggestions)

if __name__ == "__main__":
    app.run(debug=True)