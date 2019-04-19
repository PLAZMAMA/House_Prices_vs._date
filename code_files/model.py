from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection
import pandas as pd
import numpy as np

#loading the data
df = pd.read_csv("/Users/maor/Documents/src/house_prices_vs._date/date_vs_price.csv")

#creating the xs and ys
xs = df[['sqft_living']]
ys = df[['price']]

#creaing the training and testing data for the model
x_train, x_test, y_train, y_test = model_selection.train_test_split(xs, ys, test_split = 0.3)

#defining and training the model
model = LinearRegression(n_jobs = -1)
model.fit(x_train, y_train)