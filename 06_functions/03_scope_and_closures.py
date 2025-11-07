# The Scope Hierarchy (LEGB Rule):
#
# L → Local (inside current function)
# E → Enclosing (inside any outer functions)
# G → Global (top-level of the file)
# B → Built-in (Python’s internal names like len, print)


# -------------------------------------------------------
# 1. LOCAL VS GLOBAL SCOPE
# -------------------------------------------------------

x = 10  # Global variable

def show_number():
    x = 5   # Local variable (only visible inside function)
    print("Inside function, x =", x)

show_number()
print("Outside function, x =", x)


# -------------------------------------------------------
# 2. MODIFYING GLOBAL VARIABLES
# -------------------------------------------------------

count = 0

def increment_global():
    global count
    count += 1
    print("Inside function, count =", count)

increment_global()
print("Outside function, count =", count)


# -------------------------------------------------------
# 3. NONLOCAL VARIABLES
# -------------------------------------------------------

def outer():
    x = 10
    def inner():
        nonlocal x   # Use the variable from the nearest enclosing function scope, not from global or local.
        x += 5
        print("Inner x =", x)
    inner()
    print("Outer x =", x)

outer()


# -------------------------------------------------------
# 4. CLOSURES
# -------------------------------------------------------

# A closure occurs when an inner function remembers values from its enclosing scope even after that scope has finished executing.

def make_multiplier(factor):
    def multiply_by(n):
        return n * factor
    return multiply_by   # returning the inner function

double = make_multiplier(2)   # outer is done — its scope should be gone!
triple = make_multiplier(3)

print("Double 5 =", double(5))   # but inner still prints n*factor
print("Triple 5 =", triple(5))
# A closure only comes into existence when a function (the inner one) is returned or otherwise passed out of the scope where it was defined, and still needs access to variables that belong to that now-finished scope.


# Every function object in Python has an attribute __closure__ that stores the “remembered” variables.
print(triple.__closure__[0].cell_contents)


# -------------------------------------------------------
# 5. INSPECTING A CLOSURE
# -------------------------------------------------------

print(double.__closure__)           # shows captured variables
print(double.__closure__[0].cell_contents)


# Write a function that returns another function which, when called, increments and returns an internal count.

# def make_counter():
#     count = 0
#     def inner_counter():
#         nonlocal count
#         count += 1
#         return count
#     return inner_counter  # Return the function, don’t call it yet!
#
# # Create the closure
# counter = make_counter()
#
# # Each call remembers the previous count
# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3
# print(counter())  # 4
# print(counter())  # 5
# print(counter())  # 6
# print(counter())  # 7
# print(counter())  # 8