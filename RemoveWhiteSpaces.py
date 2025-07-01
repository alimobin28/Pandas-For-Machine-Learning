'''
In this file we will be removing whitespaces using three methods 

strip() : from left to right
lstrip() : from only left side
rstrip() : from only right side
'''

import pandas as pd

data = ["\nAli\n\n" , "\tTAahaa\t","\bhanI\n","baSSit","uSMANn ahmed\b"]

s = pd.Series(data)

print(s)

print("Removing WhiteSpaces and special chars using Strip() : ")

print(s.str.strip("\n\t\b"))



print("Removing WhiteSpaces and special chars using lStrip() : ")

print(s.str.lstrip("\n\t\b"))


print("Removing WhiteSpaces and special chars using rStrip() : ")

print(s.str.rstrip("\n\t\b"))