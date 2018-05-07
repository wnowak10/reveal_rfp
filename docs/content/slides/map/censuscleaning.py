# censuscleaning.py
import pandas as pd
year = 16
race = 'black'
filename = 'rawMapData/ACS_' + str(year) + '_5YR_B19001B_with_ann.csv'

df = pd.read_csv(filename, encoding='latin-1', header=1)
# print(df[df['Geography'].str.contains('California')])
# print(df.tail())

df['percent_poor'] = (df['Estimate; Total: - Less than $10,000']
                      + df['Estimate; Total: - $10,000 to $14,999']
                      + df['Estimate; Total: - $15,000 to $19,999']) / df['Estimate; Total:']

# df['County'], df['State'] =
df['County'] = df['Geography'].str.split(",", expand=True)[0]
df['State'] = df['Geography'].str.split(",", expand=True)[1]
# print(df['Geography'].str.split(",", expand=True))

# df['State'] = df['Geography'].str.split(",")[1]
df['id'] = df['Id2']

# # # # print(df[df['State'].str.contains('California')])
cols = ['id', 'County', 'State', 'percent_poor', "Estimate; Total:", "Estimate; Total: - Less than $10,000", "Estimate; Total: - $10,000 to $14,999", "Estimate; Total: - $15,000 to $19,999", "Estimate; Total: - $20,000 to $24,999", "Estimate; Total: - $25,000 to $29,999", "Estimate; Total: - $30,000 to $34,999", "Estimate; Total: - $35,000 to $39,999",
        "Estimate; Total: - $40,000 to $44,999", "Estimate; Total: - $45,000 to $49,999", "Estimate; Total: - $50,000 to $59,999", "Estimate; Total: - $60,000 to $74,999", "Estimate; Total: - $75,000 to $99,999", "Estimate; Total: - $100,000 to $124,999", "Estimate; Total: - $125,000 to $149,999", "Estimate; Total: - $150,000 to $199,999", "Estimate; Total: - $200,000 or more"]
# # # # cols2keep = cols + dist_Cols
# # # # print(cols2keep)
keep = df[cols]

print(keep.tail())

keep.to_csv('MapData/{}{}map.csv'.format(race, str(year)))

# print(keep[keep['State'] == 'California'])
