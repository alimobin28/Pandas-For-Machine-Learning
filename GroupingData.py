import pandas as pd

data = { 
    "Player" : ["Ali","Tahaa","Hani","Basit"],
    "rank" : [1,2,3,4],
    "Runs" : [40,50,60,70],
    "Year" : [2019,2020,2021,2022]
}

df = pd.DataFrame(data)

print(df)
print("\n\n")


# group by player
resdf = df.groupby("rank")
print(resdf.first())

# Iterate 
print("\n")
for Player,Runs in resdf:
    print(Player)
    print(Runs)

# view group
print(df.groupby("Player").groups)

