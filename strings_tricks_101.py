print("##########Checking if two words are anagrams##################")

# Checking if two words are anagrams
from collections import Counter

str1 = "shokr"
str2 = "shokr"

print(Counter(str1) == Counter(str2))
print("#################Reverse a String##############")

# Reverse a String

a = 'vivalaegyptehishokrbyagoodluk'
print("original string: ", a)
print (" ")
print("Reverse a String with special case of slice step")
print(" ")
print("reversied string: ")
print(a[::-1])

print("Reverse a String with loop")
for char in reversed(a):
    print(char)


print("Reverse s integer through type Conv & sliceing")

num = 23031994
print(int(str(num)[::-1]))

print("##########Transpose 2d array##########")

original = [['a','b'],['c','d'],['e','f']]
transposed = zip(*original)
print(list(transposed))

print("##########Chained Comparison##########")

b = 6
print(4 < b < 7)
print(1 == b < 20)

print("##########Dictionary Get##########")

d = {'a': 1,'b': 2}
print(d.get('c',3))
print(d)

"""pythonic way of value swap"""

a, b = "love", "peace"
print(a, b)

a, b = b, a
print(a, b)
