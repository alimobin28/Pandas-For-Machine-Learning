# 1) create a Pandas DataFrame 


import pandas as pd

data ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "marks" : [40,50,60,70]
}

df = pd.DataFrame(data)

print("Student Records\n",df)


print("\n")
# 2) Access a group of Rows and Columns in PD df

df1 = pd.DataFrame(data,index = ["Student A","Student B","Student C","Student D"])

print("Student Records\n",df1)

print("\n")

# 2a) Access the Value in Student Column Corresponding to RowA
print("Acessing Ali in Data Table\n")
print("Value =",df1.loc["Student A","student"])

print("\n")

# 3) Access a group of rows/Columns by integer position in PD DF

#printing entire row/col

print(df1.iloc[[1,2]]) # starts with 0

#4) Iterating a Column 
print("\n")
print("Printing Columns : \n")
for col in df:
    print(col)


