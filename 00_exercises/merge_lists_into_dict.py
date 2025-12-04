# Task 5: Merge two lists into a dictionary
#
# You’re given two lists:
#
# ```
# keys   = ["name", "age", "city"]
# values = ["Vivek", 22, "Kolkata"]
# ```
#
# Write a program that creates a dictionary like:
#
# ```
# {"name": "Vivek", "age": 22, "city": "Kolkata"}
# ```
#
# Rules:
# • Don’t use `zip()`
# • Don’t use dict comprehensions
# • Just loops and indexing

key = ["name", "age", "city"]
val = ["Vivek", 22, "Kolkata"]
dict = {}
for i in range(0, len(key)):
    dict[key[i]] = val[i]
print(dict)

# With zip():
keys = ["name", "age", "city"]
values = ["Vivek", 22, "Kolkata"]

result = dict(zip(keys, values))
print(result)

# With a dictionary comprehension:
keys = ["name", "age", "city"]
values = ["Vivek", 22, "Kolkata"]

result = {k: v for k, v in zip(keys, values)}
print(result)