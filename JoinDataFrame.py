# this file works on the Joining of two Data Frames using Join 

import pandas as pd
data1 ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "marks" : [40,50,60,70]
}

data2 = { 
    "RollNum" : [100,101,102,103],
    "Address" : ["ABC","DEF","GHI" ,"IJK"]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print("\n")
print(df2)
df = df1.join(df2)
print("\n")

print("Student Records\n",df)
