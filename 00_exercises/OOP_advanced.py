# 1. Create a class method that keeps count of how many objects were created.
# 2. Implement composition
#    Car has an Engine object.
# 3. Create an abstract base class Shape
#    Child classes: Circle, Rectangle
#    Implement area().

#1
class Employee:
    count = 0
    def __init__(self, name, department):
        self.name = name
        self.department = department
        Employee.count += 1

    # class method in Python is a method that is bound to the class itself, not to an instance of the class.
    # It can be called on the class directly or via an instance, and it receives the class as its first parameter (conventionally named cls), rather than the instance (self).
    @classmethod
    def get_employee_count(cls):
        return cls.count

e1 = Employee("John", "Software Engineer")
e2 = Employee("Alice", "Data Scientist")
e3 = Employee("Bob", "System Administrator")
print(e1.get_employee_count())
print(Employee.get_employee_count())

# 2
class Car:
    def __init__(self):
        print("This is a car!")
    def engine(self):
        print("This car has an engine!")

class RenaultCar:
    def __init__(self):
        self.car_obj = Car()
        print("This is a renault car!")
    def component(self):
        self.car_obj.engine()

car_obj2 = RenaultCar()
car_obj2.component()

# 3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, name):
        self.name = name
        print(f"This is a {self.name}")

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

print("Area: ", Rectangle(25, 10).area())
print("Area of circle: ", round(Circle(10).area(), 3))