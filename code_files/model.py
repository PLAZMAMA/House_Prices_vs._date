from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import preprocessing, model_selection
import pandas as pd
import numpy as np

#loading the data and extracting the valueable info
df = pd.read_csv("/Users/maor/Documents/src/house_prices_vs._date/date_vs_price.csv")
sqft = np.array(df[['sqft_living']], dtype = np.float64)
prices = np.array(df[['price']], dtype = np.float64)

plt.scatter(prices, sqft)
plt.show()