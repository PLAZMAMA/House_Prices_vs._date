import pandas as pd

df = pd.read_csv('/Users/maor/Documents/src/house_prices_vs._date/kc_house_data.csv', index_col = 0)
df = df[['date', 'price']]

df = df.sort_values('date') #sorting the date from latest to most recent
df.to_csv("/Users/maor/Documents/src/house_prices_vs._date/date_vs_price.csv")