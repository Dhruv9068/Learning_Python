
'''Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.'''



thisset = {"apple", "banana", "cherry"}
print(thisset)


#Set Items
#Set items are unordered, unchangeable, and do not allow duplicate values.


#Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

