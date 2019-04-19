import pandas as pd

#loading the original dataset and taking the valueable columns form it
df = pd.read_csv('/Users/maor/Documents/src/house_prices_vs._date/kc_house_data.csv', index_col = 0)
df = df[['sqft_living', 'price']]

#sorting the sqft of living from smallest to biggest and saving it
df = df.sort_values('sqft_living')
df.to_csv("/Users/maor/Documents/src/house_prices_vs._date/date_vs_price.csv")