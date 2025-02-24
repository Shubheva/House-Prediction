from sklearn.linear_model import LinearRegression #imports linear regression from skicit library
from sklearn.model_selection import train_test_split #splits data in to training data and testing data
import joblib #for loading the model
import pandas as pd #handles tablular data
import numpy as np

# Load dataset
df = pd.read_csv('house-prices-data.csv')  #Loads the data
print(df.columns) #debugging statement to verify my columns

# Include location as a feature
features = ["Bedrooms", "Bathrooms", "Size", "Location"] #Input variables
X = df[features] #contains input data
Y = df["Price"] # contains targer prediction output

# One-hot encode the location
X = pd.get_dummies(X, columns=["Location"], drop_first=True) #converts categorical data in to numerical data

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42) #splits the data in to training and testing.
#Here 50% data is used as testing data

# Train the model
model = LinearRegression() #Call the instance of Linear Regression Model
model.fit(X_train, Y_train) #Train the data

# Save model and columns for later use
joblib.dump((model, X.columns), "savedmodel.pkl") #Saves the trained data in to savedmodel.pkl
print("Model trained successfully and saved as 'savedmodel.pkl'")





