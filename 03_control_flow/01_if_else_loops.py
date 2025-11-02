# -------------------------------------------------------
# 1. CONDITIONALS (if, elif, else)
# -------------------------------------------------------

temperature = float(input("Enter current temperature (°C): "))

if temperature > 35:
    print("It's scorching hot! Stay hydrated.")
elif 25 <= temperature <= 35:
    print("Warm and pleasant weather.")
elif 15 <= temperature < 25:
    print("Cool breeze — perfect for a walk.")
else:
    print("It's quite chilly!")

print("End of weather report.\n")

# -------------------------------------------------------
# 2. COMPARISON AND LOGICAL OPERATORS
# -------------------------------------------------------

age = int(input("Enter your age: "))

# if 18 <= age <= 60:  # simplified chained comparison
if age >= 18 and age <= 60:
    print("You are an adult in working age.")
elif age > 60:
    print("You are a senior citizen.")
else:
    print("You are underaged.")

# Logical operators: and, or, not
has_id = True
has_ticket = False

if has_id and has_ticket:
    print("Access granted.")
elif has_id and not has_ticket:
    print("You need a ticket to enter.")
else:
    print("No entry without ID.")

print("\n")

# -------------------------------------------------------
# 3. NESTED IF STATEMENTS
# -------------------------------------------------------

score = int(input("Enter your exam score: "))

if score >= 90:
    if score >= 95:
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade: {grade}")

# -------------------------------------------------------
# 4. FOR LOOPS
# -------------------------------------------------------

print("\nFOR LOOP EXAMPLES\n")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Range-based loop
for i in range(1, 6):
    print(f"Counting: {i}")

# Sum of numbers using loop
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10 = {total}")

# -------------------------------------------------------
# 5. WHILE LOOPS
# -------------------------------------------------------

print("\nWHILE LOOP EXAMPLES\n")

n = 5
while n > 0:
    print(f"Countdown: {n}")
    n -= 1
print("Blast off!")

# User input loop
password = ""
attempts = 0
while password != "python123" and attempts < 3:
    password = input("Enter password: ")
    attempts += 1

if password == "python123":
    print("Access granted.")
else:
    print("Too many failed attempts!")

# -------------------------------------------------------
# 6. BREAK, CONTINUE, PASS
# -------------------------------------------------------

print("\nSpecial loop controls\n")

# BREAK — exit loop early
for num in range(1, 10):
    if num == 5:
        print("Breaking at 5")
        break
    print(num)

# CONTINUE — skip current iteration
for num in range(1, 10):
    if num % 2 == 0:
        continue  # skip even numbers
    print(f"Odd number: {num}")

# PASS — placeholder for future code
for _ in range(3):
    pass  # does nothing (placeholder)