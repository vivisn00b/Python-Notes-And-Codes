# Class method: @classmethod decorator is a built-in function decorator that is an expression that gets evaluated after your function is defined.
# A class method receives the class as an implicit first argument, just like an instance method receives the instance.
# A class method is a method that is bound to the class and not the object of the class.
# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
# It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that will be applicable to all the instances.
# We generally use the class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases.
class MyClass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def create(cls, value):     # instead of self, it receives the class itself → cls
        return cls(value)

obj = MyClass.create(5)     # What happened internally:
                            # cls == MyClass
                            # return MyClass(10)
print(obj.value)

# Why not use __init__ directly?
# Because: config may come from env / file / secrets manager
#          logic doesn’t belong in __init__
#          allows multiple creation paths


# Static method: A static method does not receive an implicit first argument.
# A static method is also a method that is bound to the class and not the object of the class.
# This method can't access or modify the class state.
# We generally use static methods to create utility functions.
class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_value(data):     # receives nothing: no self, no cls
        return data

print(MyClass.get_value(10))  # Output: 10

# Why static?
# does not depend on object
# does not depend on class
# just logically grouped

# Static method vs normal function
# Why not just write: def get_value(data)
# Because: logically belongs to the class
#          improves discoverability
#          improves readability in large codebases

# Example:
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))