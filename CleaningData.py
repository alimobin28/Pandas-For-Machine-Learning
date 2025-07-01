'''
This file includes Fucntion which Cleans Data 

1) isnull() : find null vals and replace with True
2) notnull() : find the NOT null vals and replace then with True
3) df.dropna() : Drop rows with NULL Valus
4) df.fillna(x) : Replace NULL values with a specific value
'''

import pandas as pd

df = pd.read_csv("C:\\Users\\alimo\\OneDrive\\Documents\\studentRecord1.csv")

print(df)


resDf = df.isnull()

print(resDf)

resDf1 = df.notnull()

print(resDf1)

resDf2 = df.dropna()

print(resDf2)


resDf3 = df.fillna(99)

print(resDf3)