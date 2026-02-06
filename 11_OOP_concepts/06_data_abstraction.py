# Abstraction hides the internal implementation details while exposing only the necessary functionality.
# It helps focus on "what to do" rather than "how to do it."
# Types of Abstraction:
# Partial Abstraction: Abstract class contains both abstract and concrete methods.
# Full Abstraction: Abstract class contains only abstract methods.
from abc import ABC, abstractmethod
# Abstract Base Classes (ABC)

class Dog(ABC):     # this class cannot be instantiated
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def sound(self):     # Abstract Method
        pass
    def display_name(self):     # Concrete method
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):     # Partial Abstraction
    def sound(self):
        print("Labrador woofs!")

class Beagle(Dog):       # Partial Abstraction
    def sound(self):
        print("Beagle barks!")

dogs = [Labrador("Max"), Beagle("Roxie")]
for dog in dogs:
    dog.display_name()
    dog.sound()
