# Sorting the DataFrame in Both Ascending and Descending

import pandas as pd

data ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [3,1,2,1],
    "marks" : [40,50,60,70],
    "RollNum" : [100,101,102,103],
    "Address" : ["ABC","DEF","GHI" ,"IJK"]
}

df = pd.DataFrame(data,index=[1,2,3,4])

print("Student Records\n",df)

res = df["rank"].duplicated()
print("Describing Duplicates : ")
print(res)



res1 = df["rank"].drop_duplicates()
print(res1)