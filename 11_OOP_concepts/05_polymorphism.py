# Polymorphism: means "same operation, different behavior." It allows functions or methods with the same name to work differently depending on the type of object they are acting upon.
#
# Compile-Time Polymorphism: This type of polymorphism is determined during the compilation of the program.
# It allows methods or operators with the same name to behave differently based on their input parameters or usage.
# In languages like Java or C++, compile-time polymorphism is achieved through method overloading, but it's not directly supported in Python.
# Python mimics it using default arguments or *args/**kwargs.
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))
print(calc.add(1, 2, 3, 4))

# Run-Time Polymorphism: It is determined during the execution of the program. It covers multiple forms in Python:
#
# 1. Method Overriding: A subclass redefines a method from its parent class.
# 2. Duck Typing: If an object implements the required method, it works regardless of its type.
# 3. Operator Overloading: Special methods (__add__, __sub__, etc.) redefine how operators behave for user-defined objects.

# Method overriding
class Animal:
    def speak(self):
        return "I'm an animal..."
class Dog(Animal):
    def speak(self):
        return "Woof!"
print(Dog().speak())

# Duck typing: Duck Typing is a type system used in dynamic languages
# We check for the presence of a given method or attribute
# Object must have the minimum necessary attributes/methods
class Cat:
    def speak(self):
        return "Meow!"
def speaking_animal(animal):     # This function works for both Dog and Cat because they both have a 'speak' method
    return animal.speak()
print(speaking_animal(Cat()))
print(speaking_animal(Dog()))

class Bird:
    def fly(self):
        print("fly with wings")
class Airplane:
    def fly(self):
        print("fly with fuel")
class Fish:
    def swim(self):
        print("fish swim in sea")
# Attributes having same name are
# considered as duck typing
## for obj in Bird(), Airplane(), Fish():
##     obj.fly()     # no fly attribute in Fish so it'll give an error

# Operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # This special method defines the behavior of the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)     # creates a brand new Vector object
        # return self.x + other.x, self.y + other.y           # becomes a tuple, not a Vector; dot function won't work
    def __repr__(self):
        return f"({self.x}, {self.y})"
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)
print(v3.x)  # as object was created attributes can be accessed with dot function
v1_0 = Vector("Hello", "Python" )
v2_0 = Vector("World", "World" )
print(v1_0 + v2_0)

# overloading both < and == operators for custom comparisons.
class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        return "ob1 is less than ob2" if self.a < other.a else "ob2 is less than ob1"
    def __eq__(self, other):
        return "Both are equal" if self.a == other.a else "Not equal"

ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print(ob3 == ob4)