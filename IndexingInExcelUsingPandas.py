# Indexing in Pandas 

# There are three ways for indexing when reading from excel

# 1) using [] 2) using loc and 3) using iloc

import pandas as pd

df = pd.read_excel("C:\\StudentRec.xlsx",index_col="Student")

print(df)
#first method
res = df["Marks"]

#second method
print(df.loc["usman"])

#third method

print(df.iloc[3])

