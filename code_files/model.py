from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, model_selection
import pandas as pd
import numpy as np
import pickle as pk

#loading the data
df = pd.read_csv("/Users/maor/Documents/src/house_prices_vs._date/sqft_vs_price.csv")

#creating the xs and ys
xs = df[['sqft_living']]
ys = df[['price']]

#creaing the training and testing data for the model
x_train, x_test, y_train, y_test = model_selection.train_test_split(xs, ys, test_size = 0.3)

#defining and training the model
model = LinearRegression(n_jobs = -1)
model.fit(x_train, y_train)

#getting the accuracy of the model
accuracy = model.score(x_test, y_test)
print(accuracy)

#saving the model with pickle
with open("/Users/maor/Documents/src/house_prices_vs._date/linear_regression_model.pickle", "wb") as m:
    pk.dump(model, m)