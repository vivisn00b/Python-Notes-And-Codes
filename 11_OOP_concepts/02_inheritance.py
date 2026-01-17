# Inheritance: allows a class (child class) to acquire properties and methods of another class (parent class).
# It supports hierarchical classification and promotes code reuse.
# In short, child class reuses behavior of parent class
# Inheritance is also called an Is-A Relation.
#
# Types of Inheritance:
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from more than one parent class.
# Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print(f"Doggo's name is {self.name}")

# Single inheritance
class Labrador(Dog):
    def sound(self):
        print("Labrador swoofs")

# Multilevel inheritance
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} guides the wayyy!")

class Friendliness:
    def greet(self):
        print("Friendly greeting")

class GoldenRetriever(Dog, Friendliness):
    def sound(self):
        print("Golden retriever barks!!!")

lab = Labrador("Buddy", 2)
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max", 4)
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie", 1)
retriever.display_name()
retriever.greet()
retriever.sound()

# super() – calling parent logic
class DataSource:
    def extract(self):
        print("Extracting data")

class CSVSource(DataSource):
    def extract(self):
        super().extract()
        print("CSV parsing logic")

csv_source = CSVSource()
print(csv_source.extract())