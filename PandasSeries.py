# Mostly like Array

import pandas as pd

data = [10,20,40,80,100]

 #s = pd.Series(data,index = ["Row A","Row B","Row C","Row D","Row E"])

s = pd.Series(data)
# print("\n")
print("Series:")
print(s)

print("Value : ",s[2])

s1 = pd.Series(data,index = ["Row A","Row B","Row C","Row D","Row E"])
print("\n")
print(s1)

# Accessing from labels(index)

print("Value Accessed from labels : ")