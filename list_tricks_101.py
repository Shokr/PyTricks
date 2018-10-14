#Create a single string from all the elements in list

a = ["python", "is", "awesome"]
print(" ".join(a))


print("##########Find The Most Frequent Value In A List.##################")
# Find The Most Frequent Value In A List.

a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1, 2, 3]

print(max(set(a), key=a.count))
print("############################")

# using counter from collection

from collections import Counter

cnt = Counter(a)
print(cnt.most_common(3))

print("## Reverse a list ##")
# Reverse a list

a = [5,4,3,2,1]
print(a[::-1])

for element in reversed(a):
    print(element)

print("######Copying List######")

print("# Copying List #")

print("### a fast way to make a shallow copy of a list ###")

b = a
b[0] = 10
print(b)

print ("### only b will changed ###")

b = a[:]
b[0] = 10 
print(b)

print (" # copy list by typecasting method")

a = [1,2,3,4,5]
print(list(a))

print("# using list.copy #")

b = a.copy()
print(b)

print(' ==> copy nested lists using copy.deepcopy ..')

from copy import deepcopy

l = [[1, 2] , [3, 4], [5, 6]]

l2 = deepcopy(l)
print(l2)

print("#########################")

# Convert list to comma separated

print("## Convert list to comma separated string ##")

items = ['foo','bar','xyz']
print (','.join(items))


print("## list of mix data ##")
data = [2,"hello", 3, "hi"]
print (','.join(map(str, data)))

# Min and Max index in List

print("## find Min / Max index in List ##")

lst = [40,10,20,30,50]

def minIndex(lst):
    return min(range(len(lst)), key=lst.__getitem__)

def maxIndex(lst):
    return max(range(len(lst)), key=lst.__getitem__)

print(minIndex(lst))
print(maxIndex(lst))


"""Remove duplicates from a list"""
print("--> Remove duplicates from a list & keep order <--")

from collections import OrderedDict

items = ["my", "name", "is", "python", "name", "is", "is"]

clear_llist = list(OrderedDict.fromkeys(items).keys())

print(items)
print(clear_llist)
