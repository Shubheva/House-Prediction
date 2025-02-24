# House Price Prediction Web Application

This application predicts the prices of house based on various features like Number of Rooms, Number of Bathrooms, Size of the house and Location.
I have made use of simple Linear Regression Model to predict the house prices.

## Linear Regression Model
It is a statistical model which predicts output (y) based on various features assuming a linear relationship between input and output.
Motivation: I decided to use linear regression model as it is simple to understand, easily interpretable and effective.
It works well with the numeric values as well as categorical data using one-hot encoding.
Sometimes, it may cause problem if the relationships are non linear. Also, it is observedthat this model is sensitive with outliers. That is extreme low or extreme high values may cause wrong predictions.
Linear Regression Model provides benchmark for more advanced models.
To improve the predictions we can use more complex models like KNN algorithm, Decision trees, Random Forest etc.

Here For programming I have considered 4 features which are size of the house, number of bedrooms, number of bathrooms and location.
Except Location every thing is numerical data, so linear regression model can be applied directly. In case of location, one-hot encoding has been used. It is the method which converts categorical data to mathematical data.

## Implementation Steps:

### Step 1: Clone the Github repository

### Step 2: Download the required Libraries
1. Numpy
2. Scikit-learn
3. Pandas
4. numpy

Command:
pip install Numpy Scikit-learn Pandas numpy

### Step 3: Different Files and their paths

Different files can be found with this project
/templates/Houseform.html: In this file, the main form has been designed
/templates/result.html:Here the predicted result is designed

/static/resultstyle.css: Contains the styles for result page
/static/style.css: Contains the styles for main house form

app.py: This is the python file where the actual flask application has been programmed.

model.py: Contains the program for machine learning model

savedmodel.pkl: Saves the trained model

house-prices-data.csv: Open source data for house prediction
Here I have considered any available data from opensource.

### Step 4: Check the paths
Make sure you save html files in templates folder and css files in static folder.
Also, before executing the files please make sure to navigate to the respective folder where these files are saved.

Command: cd House_Prediction

### Step 5: Steps to run the codes.
#### python model.py  

Example output:  
Index(['Price', 'Size', 'Bedrooms', 'Bathrooms', 'Location'], dtype='object')
Model trained successfully and saved as 'savedmodel.pkl'  

#### python app.py  

Example output:  
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: 105-716-319

You will have to click the server address (http://127.0.0.1:5000; may be differnt in your case) for the final application.

## Future Perspectives:
We can improve this application by using other powerful machine learning models as stated above
We can connect this application with a powerful database such that each detail of the user is saved.
In this project I have focussed the metropolitian cities. But in future we may dive deep by taking the location as per areas in the cities
Also, this application is for house price prediction, In similar pattern we can design the application which predicts the house rent for the user.


