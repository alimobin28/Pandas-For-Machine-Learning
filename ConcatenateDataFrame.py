import pandas as pd
data1 ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "marks" : [40,50,60,70]
}

data2 = { 
    "student" : ["Qadir","Usman","Hadi","Mustafa"],
    "rank" : [5,6,7,8],
    "marks" : [80,65,90,69]
}

df1 = pd.DataFrame(data1,index=["Student 1","Student 2","Student 3","Student 4"])
df2 = pd.DataFrame(data2,index=["Student 5","Student 6","Student 7","Student 8"])
print(df1)
print("\n")
print(df2)
df = pd.concat([df1,df2])
print("\n")

print("Student Records\n",df)
