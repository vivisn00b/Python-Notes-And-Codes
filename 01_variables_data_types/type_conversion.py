# -------------------------------------------------------
# 1. EXPLICIT TYPE CONVERSION (type casting)
# -------------------------------------------------------

# You can convert one type to another using constructor functions:
# int(), float(), str(), bool(), list(), tuple(), set(), dict(), etc.

# Example: Converting string to number
a = "123"
print("Original:", a, type(a))

b = int(a)           # string → int
c = float(a)         # string → float
d = str(b)           # int → string again
e = bool(a)          # non-empty string → True

print("\nAfter conversions:")
print("b =", b, type(b))
print("c =", c, type(c))
print("d =", d, type(d))
print("e =", e, type(e))

# Watch what happens with invalid conversions
try:
    invalid = int("abc")  # "abc" is not numeric
except ValueError as err:
    print("\nInvalid conversion example:", err)

# Example: Converting data structures
numbers_list = [1, 2, 3]
numbers_tuple = tuple(numbers_list)
numbers_set = set(numbers_list)

print("\nData structure conversions:")
print("list → tuple:", numbers_tuple)
print("list → set:", numbers_set)

# Converting to bool: Python treats some values as False automatically.
# "Falsy" values: False, 0, 0.0, '', [], {}, set(), None
print("\nBoolean conversions:")
print("bool(0)     =", bool(0))
print("bool('')    =", bool(''))
print("bool([])    =", bool([]))
print("bool([1])   =", bool([1]))
print("bool('Hi')  =", bool("Hi"))

# -------------------------------------------------------
# 2. IMPLICIT TYPE CONVERSION (type coercion)
# -------------------------------------------------------

# When Python automatically converts types in expressions.
# Example: int + float → float
x = 10      # int
y = 2.5     # float
result = x + y
print("\nImplicit conversion:")
print(f"{x} + {y} = {result} ({type(result)})")

# Example: bool + int → int
print("True + 4 =", True + 4)   # True acts as 1
print("False + 4 =", False + 4) # False acts as 0

# Python won’t mix incompatible types automatically
try:
    bad = "5" + 5
except TypeError as err:
    print("\nImplicit conversion error:", err)

# -------------------------------------------------------
# 3. PRACTICAL EXAMPLES
# -------------------------------------------------------

# Example 1: Get user input and safely convert
# (uncomment if running interactively)
# age_str = input("\nEnter your age: ")
# age = int(age_str)
# print(f"You'll be {age + 1} next year.")

# Example 2: Convert floating-point result to int
price = 19.99
items = 3
total_cost = price * items
rounded_cost = int(total_cost)   # chopping off decimal
print("\nPractical conversion:")
print(f"Total before rounding: {total_cost}")
print(f"Total after rounding to int: {rounded_cost}")

# Example 3: Using round() for controlled rounding
rounded_cost = round(total_cost, 2)
print("Rounded cost (2 decimals):", rounded_cost)
