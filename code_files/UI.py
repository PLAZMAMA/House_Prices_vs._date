import pickle as pk
import numpy as np
import math

#loading the model
m = open("/Users/maor/Documents/src/house_prices_vs._date/linear_regression_model.pickle", "rb")
model = pk.load(m)

#getting the input of the user and displaying the price prediction
inpt = input("Square Feet Of Living: ")
inpt = np.array(inpt, dtype = np.float64).reshape(1, -1)
prediction = int(model.predict(inpt))
print(f"Price: {prediction}")