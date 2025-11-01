# -------------------------------------------------------
# 1. PRINTING OUTPUT
# -------------------------------------------------------

# print() sends output to the console.
# It can take multiple arguments separated by commas.
print("Hello,", "world!")     # prints with a space in between

# You can also customize the separator and ending.
print("Python", "rocks", sep="***", end="!!!\n")

# -------------------------------------------------------
# 2. FORMATTED OUTPUT
# -------------------------------------------------------

# Method 1: Old-school % formatting
language = "Python"
version = 3
print("I love %s %d" % (language, version))

# Method 2: str.format()
print("I love {} {}".format(language, version))
print("I love {0} version {1}".format(language, version))

# Method 3: f-strings (modern, clean, and fast)
print(f"I love {language} version {version}")

# f-strings can include expressions directly
a, b = 5, 3
print(f"{a} + {b} = {a + b}")

# -------------------------------------------------------
# 3. USER INPUT
# -------------------------------------------------------

# input() always returns a STRING, no matter what the user types.
name = input("What is your name? ")
print(f"Welcome, {name}!")

# To use numbers, you must convert the string to int or float.
age = int(input("Enter your age: "))
print(f"You will be {age + 1} next year!")

# -------------------------------------------------------
# 4. MULTIPLE INPUTS IN ONE LINE
# -------------------------------------------------------

# Example: Reading multiple values separated by spaces
x, y = input("Enter two numbers separated by space: ").split()
x, y = int(x), int(y)
print(f"Sum = {x + y}")

# -------------------------------------------------------
# 5. PRINT FORMATTING OPTIONS
# -------------------------------------------------------

# sep → controls what separates printed items
# end → controls what’s printed at the end (default = newline)
print("A", "B", "C", sep="-", end=" >>> ")
print("Done")

# -------------------------------------------------------
# 6. OUTPUT FORMATTING EXAMPLES
# -------------------------------------------------------

# Aligning and padding numbers
num = 123.4567
print(f"{num:.2f}")          # 2 decimal places
print(f"{num:10.2f}")        # width 10, right-aligned
print(f"{num:<10.2f}")       # left-aligned
print(f"{num:^10.2f}")       # centered

# Integer formatting
n = 42
print(f"Binary: {n:b}, Octal: {n:o}, Hex: {n:x}")

# -------------------------------------------------------
# 7. EXAMPLE PROGRAMS
# -------------------------------------------------------

# Example 1: Greeting the user
def greet_user():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to Python.")

# Example 2: Simple interest calculator
def simple_interest():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate (%): "))
    t = float(input("Enter time (years): "))
    si = (p * r * t) / 100
    print(f"Simple Interest = {si:.2f}")

# Example 3: Temperature converter
def celsius_to_fahrenheit():
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.2f}°F")

greet_user()
simple_interest()
celsius_to_fahrenheit()
