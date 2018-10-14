x = [True, True, False]

if any(x):
    print("At least one True")

if all(x):
    print("Not one False")

if any(x) and not all(x):
    print("At least one True and one False")


# dir :: look inside a Python object and see what attributes it has

print('-----------------------------=======================-----------------------')
print(dir())
print('----------------------------------------------------')
print(dir("hello World"))
print('----------------------------------------------------')
print(dir(dir))
print('----------------------------------------------------')

# -->  pprint

import requests
import pprint  # pretty print

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()

pprint.pprint(users)
print("------------------------------------------------------------------------")

"""
uuid

A quick and easy way to
 generate Universally Unique IDs (or ‘UUIDs’).
"""

import uuid

user_id = uuid.uuid4()
print(user_id)

print("------------------------------------------------------------------")

