# 01_variables_and_types.py
# Purpose: Understand variables, data types, and how Python stores information.

# -----------------------------------------
# 1. VARIABLES — names that refer to values
# -----------------------------------------

# In Python, variables are not boxes that “hold” data;
# they are *labels* (names) bound to objects in memory.
# Think of them as sticky notes pointing to values.

x = 10              # int
y = 3.14            # float
name = "Python"     # str (string)
is_cool = True      # bool
nothing = None      # special constant for 'no value'

print("Variables created:")
print(f"x = {x}, y = {y}, name = {name}, is_cool = {is_cool}, nothing = {nothing}")

# You can reassign freely — Python is dynamically typed.
x = "Now I'm a string"
print("\nAfter reassignment, x =", x)

# -----------------------------------------
# 2. DATA TYPES — Python objects come in kinds
# -----------------------------------------

# Built-in types (core primitives)
integer_example = 42
float_example = 3.14159
string_example = "Hello, world!"
boolean_example = False
none_example = None

# type() tells us what kind of object a variable refers to
print("\nData types:")
print(type(integer_example), type(float_example), type(string_example),
      type(boolean_example), type(none_example))

# -----------------------------------------
# 3. TYPE CONVERSION — casting between types
# -----------------------------------------

# Explicit conversions
a = "123"
b = int(a)          # convert string to int
c = float(b)        # convert int to float
d = str(c)          # convert float to string

print("\nType conversion examples:")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Implicit conversions (Python does them automatically when safe)
result = 5 + 2.0   # int + float => float
print("\nImplicit conversion:")
print("5 + 2.0 =", result, type(result))

# -----------------------------------------
# 4. IDENTITY AND MUTABILITY
# -----------------------------------------

# id() gives the memory address of the object a variable points to
num1 = 1000
num2 = 1000
print("\nIDs of num1 and num2:", id(num1), id(num2))
print("Are they the same object?", num1 is num2)

# Mutability: Some types can change their content, others can’t.
# Lists are mutable, strings are not.

mutable_list = [1, 2, 3]
immutable_string = "abc"

mutable_list.append(4)     # This modifies the same object
print("\nMutable list after append:", mutable_list)

try:
    immutable_string[0] = "z"   # This will raise an error
except TypeError as e:
    print("Strings are immutable:", e)

# -----------------------------------------
# 5. DYNAMIC TYPING — reassigning new types
# -----------------------------------------

item = 10        # int
print("\nInitially:", item, type(item))
item = "ten"     # now a string
print("After reassignment:", item, type(item))
item = [1, 2, 3] # now a list
print("Reassigned again:", item, type(item))

# -----------------------------------------
# 6. CONSTANTS — just naming convention
# -----------------------------------------

# Python doesn’t enforce constants, but by convention:
PI = 3.14159
GRAVITY = 9.8
print("\nConstants by convention:")
print("PI =", PI, ", GRAVITY =", GRAVITY)

# -----------------------------------------
# 7. INPUT AND SIMPLE OUTPUT (sneak peek)
# -----------------------------------------

# input() always returns a string:
name = input("\nWhat is your name? ")
print(f"Nice to meet you, {name}!")
