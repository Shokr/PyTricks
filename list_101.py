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

