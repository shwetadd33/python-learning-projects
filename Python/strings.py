Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "ice cream"
text
'ice cream'
text[0]
'i'
text[4]
'c'
text[5]
'r'
text[3]
' '
Note1 = "string are immutable in python"
Note1
'string are immutable in python'
text[0:3]
'ice'
text[4:9]
'cream'
text[4:]
'cream'
text[:3]
'ice'
text = "hello"
text = 'hello'
text = "let's learn python"
text
"let's learn python"
text = ' I will eat "Pasta"'
text
' I will eat "Pasta"'
address = '''1 purple street
new york
usa'''
address
'1 purple street\nnew york\nusa'
s1 = "hello"
s2 = "world"
s1+s2
'helloworld'
>>> s1+' '+s2
'hello world'
>>> s="total states in usa"
>>> num =25
>>> s1+num
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s1+num
TypeError: can only concatenate str (not "int") to str
>>> str(num)
'25'
>>> s+25
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s+25
TypeError: can only concatenate str (not "int") to str
>>> s+num
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s+num
TypeError: can only concatenate str (not "int") to str
>>> s+str(num)
'total states in usa25'
>>> s = 'total states in usa # '
>>> s+str(num)
'total states in usa # 25'
