# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:08:36 2023

@author: Sagar
"""

import tkinter as tk
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import joblib
import pickle
# Create the Tkinter application window
window = tk.Tk()

# Create a label for displaying the prediction result
prediction_label = tk.Label(window, text="Real-time prediction will be displayed here")
prediction_label.pack()

# Load the trained SVM model and scaler
svm_model = SVC()
with open("SVM_PCOS.pkl", "rb") as file:
    svm_model = pickle.load(file)
#svm_model.load("SVM_PCOS.pkl")  # Replace "svm_model.pkl" with the actual filename
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file) # Replace "scaler.pkl" with the actual filename
entry = tk.Entry(window)
entry.pack()

# Create a function to perform real-time prediction
def perform_prediction():
    # Get the input data from the entry widget
    input_data = entry.get()

    # Split the input string by commas and remove any leading/trailing whitespaces
    input_values = [value.strip() for value in input_data.split(',')]

    try:
        # Convert the input values to floats
        input_values = [float(value) for value in input_values]

        # Preprocess the input data (similar to the preprocessing step above)
        input_data_scaled = scaler.transform([input_values])

        # Predict the target class for the input data using the trained SVM model
        prediction = svm_model.predict(input_data_scaled)

        # Update the prediction label with the result
        prediction_label.config(text="Real-time prediction: {}".format(prediction))

    except ValueError:
        # Display an error message if the input values are not valid numbers
        prediction_label.config(text="Invalid input values")

# Create a button to trigger the prediction
button = tk.Button(window, text="Predict", command=perform_prediction)
button.pack()

# Run the Tkinter event loop
window.mainloop()