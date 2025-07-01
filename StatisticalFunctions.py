'''
In this File we will be performing Statistical Functions 
'''

import pandas as pd

data = {
    'Math': [80, 90, 70, 60, 75],
    'Science': [88, 92, 85, 78, 90],
    'English': [78, 85, 82, 75, 88]
}

df = pd.DataFrame(data)
print("Sample DataFrame:\n", df)

print("\n1. Sum of values:\n", df.sum())

print("\n2. Count of non-empty values:\n", df.count())

print("\n3. Maximum of the values:\n", df.max())

print("\n4. Minimum of the values:\n", df.min())

print("\n5. Mean of the values:\n", df.mean())

print("\n6. Median of the values:\n", df.median())

print("\n7. Standard deviation of the values:\n", df.std())

print("\n8. Summary statistics using describe():\n", df.describe())
