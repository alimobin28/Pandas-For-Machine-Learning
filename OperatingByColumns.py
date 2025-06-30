# In this file we will be seeing how to Add and delete Columns 

# Add a row/Column

# Adding Columns has two methods insert and assign

# Delete a row/Column
# .drop is used for it 

# Iterating over rows and Column

import pandas as pd

data ={
    "student" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "marks" : [40,50,60,70]
}

df = pd.DataFrame(data)

print("Student Records\n",df)

df.insert(2,"Roll number",[100,101,102,103])

print("Updated Record \n")
print(df)

resDf=df.assign(BodyCount=[8,9,10,11])

print(resDf)

#delete a row
resDf=resDf.drop(1,axis=0) # Taaha will be deleted

print("Updated Record \n")
print(resDf)

#Iterating ROWS/COLS

print("Printing Rows \n")
for rows in resDf.iterrows():
    print(rows)



print("Printing Columns \n")
for a,b in resDf.items():
    print(a)
    print(b)

    