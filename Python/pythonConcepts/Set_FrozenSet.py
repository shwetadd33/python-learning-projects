"""
Set is an unordered collection of unique elements
frozen set - can not change the contents of a Set
"""

fruits = {"orange","apple","mango","apple","mango"}

fruits.add("grape")

print(fruits)

fs = frozenset(fruits)

#####fs.add("tomato")     # This line will give an error as we can not change the frozenset

print("apple" in fruits)
print("abc" in fruits)

for i in fruits:
    print(i)

fruits_1 = {"apple","mango","Strawberry","coconut"}

# finding union of 2 sets
print(fruits|fruits_1)
# intersection of 2 sets
print(fruits&fruits_1)
# Difference of 2 sets
print(fruits_1-fruits)
print(fruits-fruits_1)
