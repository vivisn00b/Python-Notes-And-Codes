# -------------------------------------------------------
# 1. FOR LOOP — ITERATING OVER A SEQUENCE
# -------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# For loops iterate over any iterable: list, tuple, string, range, etc.
for char in "Python":
    print(char, end=" ")
print() # newline

# -------------------------------------------------------
# 2. RANGE — GENERATE SEQUENCES OF NUMBERS
# -------------------------------------------------------

# range(start, stop, step)
for i in range(1, 6):
    print(f"Count: {i}")

# Skip numbers with step
for i in range(0, 10, 2):
    print(f"Even: {i}")

# Reverse counting
for i in range(5, 0, -1):
    print(f"Reverse: {i}")

# -------------------------------------------------------
# 3. WHILE LOOP — RUN UNTIL A CONDITION BREAKS
# -------------------------------------------------------

count = 0
while count < 5:
    print(f"While count: {count}")
    count += 1

# Be careful! Infinite loops happen easily:
# while True:
#     print("Looping forever!")

# -------------------------------------------------------
# 4. LOOP CONTROL: break, continue, else
# -------------------------------------------------------

for n in range(1, 10):
    if n == 5:
        print("Breaking at 5")
        break
    print(n)
else:
    print("Loop finished naturally!")  # Won’t run if break triggers

# continue skips current iteration
for n in range(1, 6):
    if n == 3:
        continue
    print(f"Continue example: {n}")

# -------------------------------------------------------
# 5. NESTED LOOPS
# -------------------------------------------------------

for i in range(1, 4):
    for j in range(1, 4):
        print(f"Pair: ({i}, {j})")

# Useful for grids, combinations, matrix-like data

# -------------------------------------------------------
# 6. LOOPING OVER DICTIONARIES
# -------------------------------------------------------

person = {"name": "Viv", "age": 25, "city": "Paris"}

for key, value in person.items():
    print(f"{key} : {value}")

# -------------------------------------------------------
# 7. ENUMERATE — GET INDEX + VALUE
# -------------------------------------------------------

colors = ["red", "green", "blue"]

for index, color in enumerate(colors, start=1):
    print(f"{index}: {color}")

# -------------------------------------------------------
# 8. ZIP — PARALLEL ITERATION
# -------------------------------------------------------

names = ["Ava", "Ben", "Cara"]
scores = [90, 80, 95]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# -------------------------------------------------------
# 9. COMPREHENSION PREVIEW
# -------------------------------------------------------

# Build new lists in one line
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Filtered comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# -------------------------------------------------------
# Multiplication Table
# -------------------------------------------------------

number = int(input("Enter a number for its multiplication table: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")