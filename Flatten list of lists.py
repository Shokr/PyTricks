# Trick [7]: Flatten list of lists
"""
a = [[1, 2], [3, 4], [5, 6]]

Convert it to a single list without using any loops.

Output:- [1, 2, 3, 4, 5, 6]
"""

a = [[1, 2], [3, 4], [5, 6]]
print([x for _list in a for x in _list])

print("  ")
