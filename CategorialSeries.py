import pandas as pd

data1= ["p","q","r","s"]

s = pd.Series(data1,dtype="category")

print(s)

df = pd.DataFrame({"Cat1" : list("pqrs"),"Cat2" : list("rqsp")})

print(df)

print("Data types :\n",df.dtypes)

# 1) Append Category
s = s.cat.add_categories("t")

print("Updated :")
print(s)

# 2 ) Remove Category

s = s.cat.remove_categories("q")

print("Updated :")
print(s)

