# In composition, we will describe a class that references to one or more objects of other classes as an Instance variable.
# By using the class name or by creating the object we can access the members of one class inside another class.
# It enables creating complex types by combining objects of different classes. It means that a class Composite can contain an object of another class Component.
# This type of relationship is known as Has-A Relation.

class Component:
    def __init__(self):
        print("Component class object created")

    def method1(self):
        print("Component class method1 called")

class Composite:
    def __init__(self):
        self.obj1 = Component()
        print("Composite class object created")

    def method2(self):
        print("Composite class method2 called")
        self.obj1.method1()

obj2 = Composite()
obj2.method2()

# If both inheritance and composition are pointing to code reusability then  what is the difference b/w Inheritance and Composition and when to use Inheritance and when to use Composition?
# Inheritance is used where a class wants to derive the nature of parent class and then modify or extend the functionality of it.
# Inheritance will extend the functionality with extra features allows overriding of methods, but in the case of Composition, we can only use that class we can not modify or extend the functionality of it.
# Composition will not provide extra features. Thus, when one needs to use the class as it without any modification, the composition is recommended and when one needs to change the behavior of the method in another class, then inheritance is recommended.