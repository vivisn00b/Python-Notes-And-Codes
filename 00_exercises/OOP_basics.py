# 1. Create a Person class with attributes name and age.
#    Add a method introduce() that prints a sentence.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("John", 25)
p.introduce()

# 2. Create a class Rectangle
#    Attributes: length, breadth
#    Methods: area(), perimeter()
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * self.length + 2 * self.breadth

p = Rectangle(150, 90)
print("Area: ", p.area())
print("Perimeter:", p.perimeter())