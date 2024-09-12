Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={"tom":32424353,"rob":34323535,"joe":3423435}
d
{'tom': 32424353, 'rob': 34323535, 'joe': 3423435}
d["tom"]
32424353
d["Sam"] =2242342353
d
{'tom': 32424353, 'rob': 34323535, 'joe': 3423435, 'Sam': 2242342353}
del d["tom"]
d
{'rob': 34323535, 'joe': 3423435, 'Sam': 2242342353}
for key in d:
    print("key:", key, "value:" d[key])
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
for key in d:
    print("key:", key, "value:", d[key])

    
key: rob value: 34323535
key: joe value: 3423435
key: Sam value: 2242342353
for k,v in d.items():
    print("key:", k, "value:", v)

    
key: rob value: 34323535
key: joe value: 3423435
key: Sam value: 2242342353
key: Sam value: 2242342353
SyntaxError: invalid syntax

"tom" in d
False
"Joe" in d
False
"joe" in d
True

d.clear
<built-in method clear of dict object at 0x0000013BD8B63040>
>>> d
{'rob': 34323535, 'joe': 3423435, 'Sam': 2242342353}
>>> d.clear()
>>> d
{}
>>> 
>>> // Tuples is a list of vlaues group together
SyntaxError: invalid syntax
>>> '''Tuples is a list of vlaues group together'''
'Tuples is a list of vlaues group together'
>>> ''' Note: Tuples is a list of vlaues group together'''
' Note: Tuples is a list of vlaues group together'
>>> '''Note1 : Tuples is a list of vlaues group together
... '''
'Note1 : Tuples is a list of vlaues group together\n'
>>> 
>>> point=(5,9)
>>> point[0]
5
>>> point[1]
9
>>>  ''' List: all the values have similar meaning
SyntaxError: unexpected indent
>>> ''' List: all the values have similar meaning
...  Tuple: all the values have different meaning'''
' List: all the values have similar meaning\n Tuple: all the values have different meaning'
>>> 
>>> ''' Tuples are immutable'''
' Tuples are immutable'
