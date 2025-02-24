from flask import Flask, render_template, request #import render template to get data from html and retrieves data sent from user
import joblib #use to load dataset
import numpy as np #for mathematical calculation
import pandas as pd

app = Flask(__name__) #initializes flask application

# Load model and columns
model, columns = joblib.load('savedmodel.pkl') #loads model

@app.route('/') #homepage route
def home():
    return render_template('HouseForm.html') #Starts with main page of house form

@app.route('/predict', methods=['POST']) #POST because user sends the request from form
def predict():
    try:
        
        bedrooms = float(request.form.get('bedrooms')) #Get the number of bedrooms from user
        bathrooms = float(request.form.get('bathrooms')) #Get the number of bathooms from user
        size = float(request.form.get('Size')) #Get the size of house from user
        location = request.form.get('Location') #Get the prefered location

        # Prepare input with one-hot encoding
        input_data = pd.DataFrame([[bedrooms, bathrooms, size, location]], columns=["Bedrooms", "Bathrooms", "Size", "Location"])

        # One-hot encode location
        input_data = pd.get_dummies(input_data, columns=["Location"])
        
        # Ensure input aligns with model features
        input_data = input_data.reindex(columns=columns, fill_value=0)

        # Predict
        prediction = model.predict(input_data)[0] #Uses loaded model and gives the prediction

        return render_template ('result.html', prediction_text=f'Prediction of your house is ₹{prediction:,.2f}')

    except Exception as e:
        print(f"Error: {e}") # Debugging
        return render_template('HouseForm.html', prediction_text="Something went wrong. Check the input values.") #if error occurs

if __name__ == '__main__':
    app.run(debug=True)
#runs when script is executed