# Encapsulation is the bundling of data (attributes) and methods (functions) within a class.
# It restricts access to some components to control interactions.
# A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
# Types of Encapsulation:
# Public Members: Accessible from anywhere.
# Protected Members: Accessible within the class and its subclasses.
# Private Members: Accessible only within the class.
class Dog:
    def __init__(self, name, breed, age):
        self.name = name        # Public members
        self._breed = breed     # Protected members (_variable)
        self.__age = age          # Private members (__variable)
    def get_info(self):
        return f'Name: {self.name}, Breed: {self._breed}, Age: {self.__age}'
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Age must be greater than 0')

dog = Dog("Buddy", "Labrador", 3)
# Accessing public member
print(dog.name)  # Accessible
# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class
# Accessing private member using getter
print(dog.get_age())
#print(dog.__age)  # gives error as attribute is private
# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())

# Pythonic way: @property
# Modern Python uses properties, not classic getters/setters.
class User:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError("Age must be positive")
        self._age = value

u = User(21)
print(u.age)
u.age = 25
print(u.age)