# Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable.
#
# Keys are case-sensitive which means same name but different cases of Key will be treated distinctly.
# Keys must be immutable which means keys can be strings, numbers or tuples but not lists.
# Duplicate keys are not allowed and any duplicate key will overwrite the previous value.
# Internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time.
# From Python 3.7 Version onward, Python dictionary are Ordered.

# --------------------------------------------------
# Python Dictionaries — Key–Value Pairs
# --------------------------------------------------

# 1 Creating Dictionaries
print("Creating Dictionaries:")

empty_dict = {}
person = {"name": "Alice", "age": 25, "city": "Paris"}
mixed_keys = {1: "one", "two": 2, (3, 4): "tuple_key"}

print("Empty dict:", empty_dict)
print("Person:", person)
print("Mixed keys:", mixed_keys)
print("-" * 50)


# 2 Accessing and Modifying Data
print("Accessing and Modifying Data:")

print("Name:", person["name"])
print("Age using get():", person.get("age"))
print("Unknown key with get(default):", person.get("salary", "N/A"))

person["age"] = 26        # modify value
person["country"] = "France"  # add new key
print("Updated person:", person)
print("-" * 50)


# 3 Removing Items
print("Removing Items:")

person.pop("city")               # remove by key
removed = person.pop("salary", "Not found")  # safe pop with default
del person["country"]            # delete by key
key, val = person.popitem()     # removes and returns the last key-value pair
print(f"Key: {key}, Value: {val}")
print("Removed city and country:", person)
print("Result of safe pop:", removed)
person.clear()     # clear all items from the dictionary
print("-" * 50)


# 4 Iterating Through Dictionaries
print("Iterating Through Dictionaries:")

student = {"name": "Bob", "age": 21, "course": "Math"}

# for value in student.values():
# for key, value in student.items():
for key in student:
    print(f"{key} → {student[key]}")

print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))
print("-" * 50)


# 5 Dictionary Comprehension
print("Dictionary Comprehension:")

squares = {x: x * x for x in range(1, 6)}
print("Squares dict:", squares)
print("-" * 50)


# 6 Nested Dictionaries
print("Nested Dictionaries:")

users = {
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 22},
}
print("Users:", users)
print("User1 name:", users["user1"]["name"])
print("-" * 50)


# 7 Useful Methods
print("Useful Methods:")

car = {"brand": "Tesla", "model": "Model 3", "year": 2020}
print("Keys:", car.keys())
print("Values:", car.values())
print("Items:", car.items())

car.update({"year": 2024, "color": "black"})  # merge/update
print("After update:", car)
print("-" * 50)


# Mini Exercise
print("Mini Exercise:")

inventory = {"apple": 10, "banana": 5, "cherry": 20}
# Increase all stock by 5 using dict comprehension
updated_inventory = {k: v + 5 for k, v in inventory.items()}
print("Updated inventory:", updated_inventory)
print("-" * 50)
