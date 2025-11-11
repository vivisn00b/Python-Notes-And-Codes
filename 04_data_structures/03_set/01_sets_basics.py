# A Set in Python is used to store a collection of items with the following properties.
#
# No duplicate elements. If try to insert the same item again, it overwrites previous one.
# An unordered collection. When we access all items, they are accessed without any specific order, and we cannot access items using indexes as we do in lists.
# Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
# Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.

# --------------------------------------------------
# Python Sets — Unordered Collections of Unique Elements
# --------------------------------------------------

# 1 Creating Sets
print("Creating Sets:")

empty_set = set()            # empty set (NOT {})
fruits = {"apple", "banana", "cherry"}
duplicates = {"apple", "apple", "banana"}

print("Empty set:", empty_set)
print("Fruits set:", fruits)
print("Duplicates removed automatically:", duplicates)
print("-" * 50)

# typecasting list to set
s = set(["a", "b", "c"])
print(s)


# 2 Adding and Removing Elements
print("Adding and Removing Elements:")

fruits.add("mango")
fruits.add("apple")  # duplicate ignored
print("After adding mango:", fruits)

fruits.remove("banana")  # raises error if not found
fruits.discard("kiwi")   # safely remove if exists
print("After removing banana and discarding kiwi:", fruits)

popped = fruits.pop()    # removes a random element
print("Popped element:", popped)
print("After pop:", fruits)
print("-" * 50)

# Heterogeneous Element with Set
s = {"Geeks", "for", 10, 52.7, True}
print(s)


# 3 Set Operations
print("Set Operations:")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A union B →", A | B)
print("A intersection B →", A & B)
print("A difference B →", A - B)
print("A symmetric difference B →", A ^ B)
print("A is equivalent to B →", A == B)
print("A is not equivalent to B →", A != B)
print("A is subset of B →", A <= B)
print("A is proper subset of B →", A < B)
print("A is superset of B →", A >= B)
print("A is proper superset of B →", A > B)
print("A is equivalent to B →", A == B)
print("-" * 50)


# 4 Membership and Iteration
print("Membership and Iteration:")

nums = {1, 2, 3, 4, 5}
print("Is 3 in nums?", 3 in nums)
print("Iterating:")
for n in nums:
    print(n)
print("-" * 50)


# 5 Set Comprehension
print("Set Comprehension:")

squares = {x * x for x in range(6)}
print("Squares set:", squares)
print("-" * 50)


# 6 Frozen Sets — Immutable Sets
print("Frozen Sets:")

fs = frozenset([1, 2, 3])
print("Frozen set:", fs)
try:
    fs.add(4)
except AttributeError as e:
    print("Cannot modify frozenset:", e)
print("-" * 50)


# 7 Union operation on Sets
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union() function
population = people.union(vampires)

print("Union using union() function")
print(population)


# 8 Intersection operation on Sets
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Intersection using intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)


# 9 Finding Differences of Sets in Python
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

# Difference of two sets using difference() function
set3 = set1.difference(set2)
print(" Difference of two sets using difference() function")
print(set3)


# 10 Clearing Python Sets
set1 = {1,2,3,4,5,6}
print("Initial set")
print(set1)

# This method will remove all the elements of the set
set1.clear()
print("\nSet after using clear() function")
print(set1)


# Mini Exercise
print("Mini Exercise:")
set1 = {"python", "java", "c++"}
set2 = {"python", "rust", "go"}
common = set1 & set2
unique = set1 ^ set2
print("Common languages:", common)
print("Unique to each set:", unique)
print("-" * 50)
