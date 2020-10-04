import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/frankData612/data_612/master/stock_data/stocks_yahoo.csv')

print(df.head(20))

print(df.tail(15))

print(df.columns)

print(df.dtypes)

print(df.shape)

print(df.groupby('date')['beta (3Y Monthly)'].mean())
