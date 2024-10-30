"""
Note: “We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument
when we have doubts about the number of  arguments we should pass in a function.”


*args (Non-Keyword Arguments): *args in function definitions in Python is used to pass a variable number of arguments to a function.
The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.

**kwargs (Keyword Arguments): **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list.
A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.


*args receives arguments as a tuple. (a,b,c)
**kwargs receives arguments as a dictionary. {"a"="A1","b"="B1,"c"="c1"}
"""

def myFunc(*args,**kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print(args)
    print(kwargs)

myFunc('Hi','I am','Shweta', first="Hi",mid="I am", last="Shweta")


# defining car class

class Car():
    def __init__(self,*args):
        self.speed = args[0]
        self.color = args[1]


audi = Car(180,"red")
bmw = Car(230,"black")

print("Speed of an Audi:", audi.speed)
print("Color of a BMW:", bmw.color)


# defining second car class using kwargs

class Car_2():
    def __init__(self,**kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']


scorpio = Car_2(s=150, c="Yellow")
mb = Car_2(s=230,c="White")

print("Speed of scorpio:", scorpio.speed)
print("Color of mb:", mb.color)

