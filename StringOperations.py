'''
In this File we will be having six functions 

1) lower() : perform lowercase on text data
2) upper() : perform uppercase on text data
3) title() : convert text data to camel case
4) len()   : return len of each element
5) count() : count non empty cells for each column or row
6) contain() : search for a value in columns
'''

import pandas as pd

data = ["Ali" , "TAahaa","hanI","baSSit","uSMANn ahmed"]

s = pd.Series(data)

print(s)

print("LowerCase : \n")
print(s.str.lower())

print("UpperCase : \n")
print(s.str.upper())

print("Camel Data : \n")
print(s.str.title())

print("Length of each eleement\n")
print(s.str.len())

print("Count of each eleement")
print(s.count())


print("Checking if Series contains ahmed")
print(s.str.contains("ahmed"))

