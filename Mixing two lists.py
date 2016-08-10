# Trick [5]: Mixing two lists
"""
list1 = ['a', 'b', 'c', 'd']

list2 = ['p', 'q', 'r', 's']

Write a Python code to print

ap

bq

cr

ds
"""

list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']

for x, y in zip(list1,list2):
    print (x, y)

print("  ")
