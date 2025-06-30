import pandas as pd

df = pd.read_csv("xxx") # replace xxx with path of your csv file (right click and click on copy path)

print("Student Records : ")
print(df)


print("Top 5 rows \n",df.head())
print("Top 2 rows \n",df.head(2))

print("Last 5 rows \n",df.tail())
print("last 2 rows \n",df.tail(2))



df1 = pd.read_excel("xx")

print(df)