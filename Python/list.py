Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"List in Python"
'List in Python'


item_list = ["bread","pasta","fruits","veggies"]
item_list
['bread', 'pasta', 'fruits', 'veggies']
item_list[1]
'pasta'
item_list[:2]
['bread', 'pasta']
item_list[0] ="chips"
item_list
['chips', 'pasta', 'fruits', 'veggies']

Note1 = "Lists are mutable"

item_list[-1:]
['veggies']
item_list[:-1]
['chips', 'pasta', 'fruits']
>>> item_list.append("butter")
>>> item_list
['chips', 'pasta', 'fruits', 'veggies', 'butter']
>>> item_list.insert(1,"maggie")
>>> item_list
['chips', 'maggie', 'pasta', 'fruits', 'veggies', 'butter']
>>> item2 = ["tissue","hand soap"]
>>> items = item_list + item2
>>> items
['chips', 'maggie', 'pasta', 'fruits', 'veggies', 'butter', 'tissue', 'hand soap']
>>> ['bread', 'pasta']
['bread', 'pasta']
>>> items
['chips', 'maggie', 'pasta', 'fruits', 'veggies', 'butter', 'tissue', 'hand soap']
>>> item + ["soda"]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    item + ["soda"]
NameError: name 'item' is not defined. Did you mean: 'item2'?
>>> len(items)
8
>>> "bread" in items
False
>>> "pasta" in items
True
