# In this file we will be seeing how to select multiple columns ,
# there are two methods 

# 1) using df[["colname","colname2"]]
# 2) using df[df.columns[2:4]]  # 2 to  4 column
import pandas as pd

data ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "marks" : [40,50,60,70],
    "RollNum" : [100,101,102,103],
    "Address" : ["ABC","DEF","GHI" ,"IJK"]
}

df = pd.DataFrame(data)

print("Student Records\n",df)

print("Selecting only two Columns : \n",df[["rank","marks"]])

print("Selecting only two Columns : \n",df[df.columns[2:4]])