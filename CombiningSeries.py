# This file includes Combining of two series(choosing max among two) using combine function
import pandas as pd

def max(x1,x2):
    if(x1 > x2):
        return x1
    else:
       return x2
    
data1 = [1,2,8,11]
data2 = [5,0,3,9]

series1 = pd.Series(data1)
series2 = pd.Series(data2)

print("Series 1 :")
print(series1)
print("\n")
print("Series 2 :")
print(series2)

res = series1.combine(series2,max)

print("After Combining Series : ")
print(res)
