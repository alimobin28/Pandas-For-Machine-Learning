# Sorting the DataFrame in Both Ascending and Descending

import pandas as pd

data ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [3,4,2,1],
    "marks" : [40,50,60,70],
    "RollNum" : [100,101,102,103],
    "Address" : ["ABC","DEF","GHI" ,"IJK"]
}

df = pd.DataFrame(data,index= ["Student A","Student B","Student C","Student D"])

print("Student Records\n",df)


print("Ascending :\n")
print(df.sort_values(by=["rank"]))

print("Descending : \n")
print(df.sort_values(by=["rank"],ascending=False))
