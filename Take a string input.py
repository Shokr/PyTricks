# Trick [9]: Take a string input

result = map(lambda x:int(x) ,input("Enter '1 2 3 4' : ").split())
print("Output: ", list(result))
