"""
Class: Human > Properties(Name,gender,occupation) > Method(Speak,Do work, Sleep)
properties and methods forms central entity called Class.
Class is abstraction of some entity which contains common set of properties and methods:

Object: Object is an instance of a Class
"""

class Human:
    def __init__(self, n, o):            # Init function will initialize the properties of this class when instance/object is created.
        self.name = n           # Self: self here means class itself. self.name & self.occupation are properties of the class Human where as n & o are parameter passed to this class.
        self.occupation = o
    def do_work(self):           # Whenever we write any METHOD (not a function) the 1st argument is always a "self".
        if self.occupation == "Tennis Player":
            print(self.name, "plays tennis")
        elif self.occupation == "Actor":
            print(self.name, "shoots a film")
    def speaks(self):
        print(self.name, 'says how are you?')


# Create some object

tom = Human("Tom jeremy","Actor")
tom.do_work()
tom.speaks()

maya = Human("Maya Sharma","Tennis Player")
maya.do_work()
maya.speaks()