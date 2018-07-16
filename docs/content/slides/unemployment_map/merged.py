# cleanue.py

import pandas as pd 
black = pd.read_csv('black2010map.csv')

df = pd.read_csv('unemployment.csv')
df['id'] = df['id'].apply(str).str.zfill(5)
df = df[['id', 'unrate']]
print(df.head())
black = black[['id']]
print(black.head())

print(df.info())

print(black.info())
# x = pd.merge(df, black, left_on = 'id', right_on='id')
df.to_csv('ue.csv')

# print(x.head())