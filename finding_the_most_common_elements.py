# Trick [14]: Finding the most common elements in an iterable
# collections.Counter lets you find the most common

import collections

c = collections.Counter('muhammed_shokr')

print(c)
print('-------------------------------------------------------------')
print(c.most_common(3))
print('-------------------------------------------------------------')
print(c.most_common(1))