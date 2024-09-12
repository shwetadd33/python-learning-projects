book = {}
book["Shweta"]={
    'name': 'Shweta',
    'address': 'street 1 Latur',
    'phone': 98946738
}
book["Ashutosh"]={
    'name': 'Ashutosh',
    'address': 'street 2 Baramati',
    'phone': 978394043
}

import json
s = json.dumps(book) # taking dictionary 'book' and dumping to string and to json format

with open("C://shweta//Courses//Python//Working_with_JSON//book.txt","w") as f:
    f.write(s)       # writing this data to an external file

f = open("C://shweta//Courses//Python//Working_with_JSON//book.txt","r")
s = f.read()  # reading the saved data from the file
print(s)
print(type(s))

book1 = json.loads(s)  # to read this json string and parse it to json object so that we can access each item
print(book1)
print(type(book1))  # string is converted as dict

print(book1['Shweta'])
print(book1['Ashutosh'])

print(book1['Shweta']['address'])
print(book1['Ashutosh']['phone'])

for person in book1:
    print(book1[person])
