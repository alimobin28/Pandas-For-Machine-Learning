# This file includes Attributes for Data Frame (dtypes,ndim,shape , size etc)


import pandas as pd

data ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "marks" : [40,50,60,70]
}

df = pd.DataFrame(data,index = ["Student A","Student B","Student C","Student D"])

print("Student Records\n",df)
print("\n")
print("Data Types \n",df.dtypes)
print("\n")
print("Data Dimensions ",df.ndim)
print("-----------------------------")
print("Data elements ",df.size)
print("-----------------------------")
print("Data Shape(m*n)",df.shape)
print("-----------------------------")
print("Data Index",df.index)
print("-----------------------------")

print("Data Transpose \n",df.T)
print("-----------------------------")

print("Printing first 2 rows : \n")
print(df.head(2))
print("-----------------------------")
print("Printing last 2 rows : \n")
print(df.tail(2))

print("-----------------------------")