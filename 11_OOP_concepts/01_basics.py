# OOP is a way of organizing code that uses objects and classes to represent real-world entities and their behavior.
# In OOP, object has attributes thing that has specific data and can perform certain actions using methods.
#
# Class: A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.
# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator.
class Dog:
    species = 'mammal'      # Class attribute
    def __init__(self, name, age):
        self.name = name    # Instance attribute
        self.age = age      # Instance attribute

# Objects: An Object is an instance of a Class. It represents a specific implementation of the class and holds its own data.
# An object consists of:
# State: It is the attributes and reflects the properties of an object.
# Behavior: It is the methods of an object and reflects the response of an object to other objects.
# Identity: It's a unique name to an object and enables one object to interact with other objects.
dog1 = Dog("Max", 3)
#print(dog1)
print(dog1.name)
print(dog1.age)
print(type(dog1))

# Self Parameter: It is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly

# __init__ method: It is the constructor in Python, automatically called when a new object is created. It initializes the attributes of the class.
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
e = Employee("Vivek", "Data Engineer")
print(e.name)
print(e.role)

# Class Variables: These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods.
# All objects of the class share the same value for a class variable unless explicitly overridden in an object.
#
# Instance Variables: Variables that are unique to each instance (object) of a class. These are defined within the __init__ method or other instance methods.
# Each object maintains its own copy of instance variables, independent of other objects.
class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Access class and instance variables
print(dog1.species)  # (Class variable)
print(dog1.name)     # (Instance variable)
print(dog2.name)     # (Instance variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)

# Methods: It is a function that belongs to a class.
# Function → lives on its own
# Method → lives inside a class and works on an object
# Methods = what the object can DO (methods are actions, not data)
class Pipeline:
    def run(self):
        print("Pipeline running")

p = Pipeline()
p.run()