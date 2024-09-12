"""
set is unordered collection of unique items i.e no duplicates

set{1,2,3,4,5}
in set you use {}  brackets
"""

numbers = {2,4,5,2,2,4,6}
print(numbers)

even = {i for i in numbers if i%2==0}
print(even)

sqr = {i*i for i in numbers}
print(sqr)