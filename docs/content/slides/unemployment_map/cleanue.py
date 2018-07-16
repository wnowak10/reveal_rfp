# cleanue.py

import pandas as pd 
df = pd.read_csv('unemployment.csv')
df['id'] = df['id'].apply(str).str.zfill(5)

df.to_csv('ue.csv')

print(df.head())