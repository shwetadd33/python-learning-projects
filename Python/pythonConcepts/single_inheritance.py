"""
Let's take an example of Vehicle

Vehicle "Car" and Vehicle "Motorcycle" has their own properties and methods.
But the "Car" class and "MotorCycle" class are subclass of main class "Vehicle"  and share same properties of vehicle and have their own separate properties and methods.

And it can be said that the Car and Motorcycle is inherited from same class i.e. Vehicle
"""


class Vehicle:
    def general_usage(self):
        print("general use: transportation")


class Car(Vehicle):  # This is the way we inherit the class from main class
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("Specific use: commute to work,vacation with family")


class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False
        self.use_helmet = True

    def specific_usage(self):
        self.general_usage()
        print("Specific use: road trip, racing")


c = Car()
c.general_usage()
print(c.wheels)
c.specific_usage()

m = MotorCycle()
m.general_usage()
print(m.use_helmet)
m.specific_usage()

print("\n------ Use of isinstance() and issubclass() in-built functions ------")
print(isinstance(c,Car))
print(isinstance(c,MotorCycle))
print(issubclass(Car,Vehicle))

""" 
Can call the method and properties of parent class using object of derived class.
Benefits : 1.Code Reuse 2.Extensibility 3.Readability
"""
