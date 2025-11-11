# A tuple in Python is an immutable, ordered collection of elements.
# The main characteristics of tuples are being ordered, heterogeneous and immutable.

# --------------------------------------------------
# Python Tuples — Immutable Sequences
# --------------------------------------------------

# 1 Creating Tuples
print("Creating Tuples:")

empty_tuple = ()
single_tuple = (42,)
multi_tuple = (1, 2, 3, 4)

print("Empty tuple:", empty_tuple)
print("Single-element tuple (note the comma!):", single_tuple)
print("Multi-element tuple:", multi_tuple)
print("-" * 50)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('yessir')  # tuple() function can take 1 argument
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Hello',) * 3
print(tup1)


# 2 Accessing Elements
print("Accessing Elements:")

t = ("apple", "banana", "cherry")
print("Tuple:", t)
print("t[0] →", t[0])
print("t[-1] →", t[-1])     # last element
print("t[0:2] →", t[0:2])   # slicing works just like lists
print("-" * 50)


# 3 Tuple Unpacking
print("Tuple Unpacking:")

person = ("Alice", 25, "Engineer")
name, age, profession = person
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# Using * to capture remaining values
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
print("First:", first)
print("Middle:", middle)
print("Last:", last)
print("-" * 50)


# 4 Nested Tuples
print("Nested Tuples:")

nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("Access nested[1][0] →", nested[1][0])
print("-" * 50)


# 5 Tuple Immutability
print("Tuple Immutability:")

immutable = (10, 20, 30)
try:
    immutable[0] = 99
except TypeError as e:
    print("Error:", e)
print("Tuples cannot be modified after creation!")
print("-" * 50)


# 6 Tuple Operations
print("Tuple Operations:")

a = (1, 2)
b = (3, 4)
print("a + b →", a + b)         # concatenation
print("a * 3 →", a * 3)         # repetition
print("3 in b →", 3 in b)       # membership
print("len(b) →", len(b))       # length
print("-" * 50)


# 7 Tuple Methods
print("Tuple Methods:")

sample = (1, 2, 2, 3, 2)
print("sample.count(2) →", sample.count(2))
print("sample.index(3) →", sample.index(3))
print("-" * 50)


# 8 Tuple vs List Memory & Use Case
print("Why Tuples?")
print("Tuples use less memory and are faster for fixed data.")
print("Example: Coordinates, configuration values, database records.")
print("-" * 50)


# 9 Deleting a Tuple
tup = (0, 1, 2, 3, 4)
print("Tuple before deleting: ", tup)
del tup
try:
    print(tup)
except NameError:
    print("Tuple DELETED successfully!")
print("-" * 50)


# Mini Exercise
print("Mini Exercise:")
colors = ("red", "green", "blue", "yellow")
primary, *secondary = colors
print("Primary color:", primary)
print("Secondary colors:", secondary)
print("Data type of secondary: ", type(secondary))
secondary[0] = "cyan"
print("Secondary colors after changing: ", secondary)
print("-" * 50)
