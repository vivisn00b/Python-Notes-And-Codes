# -------------------------------------------------------
# 1. TERNARY CONDITIONAL (inline if)
# -------------------------------------------------------

age = int(input("Enter your age: "))

# Traditional form
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"Traditional check: You are an {status}")

# Ternary form (inline)
status = "Adult" if age >= 18 else "Minor"
print(f"Ternary check: You are an {status}")

# Use case: concise conditional expressions
temperature = float(input("Enter temperature (°C): "))
comment = "Hot" if temperature > 30 else "Cold"
print(f"The weather feels {comment}")

# -------------------------------------------------------
# 2. CHAINED COMPARISONS
# -------------------------------------------------------

score = int(input("Enter your score: "))

if 0 <= score <= 100:
    print("Valid score.")
else:
    print("Invalid score! Must be 0–100.")

# This avoids writing: if score >= 0 and score <= 100

# -------------------------------------------------------
# 3. MATCH / CASE (Python 3.10+)
# -------------------------------------------------------

# The modern replacement for long if-elif chains
# Works like switch/case from other languages but with more power.

command = input("Enter command (start, stop, pause, exit): ")

match command.lower():
    case "start":
        print("Machine started.")
    case "stop":
        print("Machine stopped.")
    case "pause":
        print("Machine paused.")
    case "exit":
        print("Exiting system...")
    case _:  # wildcard for default
        print("Unknown command!")

# -------------------------------------------------------
# 4. MATCHING COMPLEX DATA STRUCTURES
# -------------------------------------------------------

# You can pattern-match tuples, lists, and dicts too.
# Example: coordinates

point = (3, 4)

match point:
    case (0, 0):
        print("Origin point")
    case (x, 0):
        print(f"On X-axis at x={x}")
    case (0, y):
        print(f"On Y-axis at y={y}")
    case (x, y):
        print(f"Point in plane at ({x}, {y})")
    case _:
        print("Invalid input")

# -------------------------------------------------------
# 5. CONDITIONAL EXPRESSIONS INSIDE LOOPS
# -------------------------------------------------------

# Categorize numbers as even/odd in one line
numbers = [1, 2, 3, 4, 5, 6]
categories = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(f"\n{categories}")

# Same idea with f-string formatting
for n in numbers:
    print(f"{n} is {'even' if n % 2 == 0 else 'odd'}")

# -------------------------------------------------------
# 6. CONDITIONAL LOGIC WITH DICTIONARIES
# -------------------------------------------------------

# Use dictionaries instead of if/elif when mapping fixed inputs to actions.
actions = {
    "start": "Machine started.",
    "stop": "Machine stopped.",
    "pause": "Machine paused."
}

command = input("\nCommand again: ").lower()
print(actions.get(command, "Unknown command!"))

# -------------------------------------------------------
# GRADING SYSTEM (with match)
# -------------------------------------------------------

grade = input("\nEnter letter grade (A, B, C, D, F): ").upper()

match grade:
    case "A" | "A+":
        points = 4.0
    case "B":
        points = 3.0
    case "C":
        points = 2.0
    case "D":
        points = 1.0
    case "F":
        points = 0.0
    case _:
        points = None

if points is not None:
    print(f"Your GPA points: {points}")
else:
    print("Invalid grade entered!")