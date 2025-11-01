# -------------------------------------------------------
# 1. BASIC STRING FORMATTING
# -------------------------------------------------------

name = "Ada Lovelace"
age = 36
profession = "Mathematician"

# Old % formatting
print("My name is %s, I'm %d years old, and I'm a %s." % (name, age, profession))

# str.format() method
print("My name is {}, I'm {} years old, and I'm a {}.".format(name, age, profession))

# Positional and keyword formatting
print("My name is {0}, I'm {1} years old, and I'm a {2}.".format(name, age, profession))
print("My name is {name}, I'm {age} years old, and I'm a {job}.".format(name=name, age=age, job=profession))

# f-string (most modern and readable)
print(f"My name is {name}, I'm {age} years old, and I'm a {profession}.")

# -------------------------------------------------------
# 2. NUMERIC FORMATTING
# -------------------------------------------------------

pi = 3.141592653589793
print(f"\nPi rounded to 2 decimals: {pi:.2f}")
print(f"Pi with 5 decimals and width 10: {pi:10.5f}")

# Format integers with padding and alignment
n = 42
print(f"Right aligned (width 5): |{n:5d}|")
print(f"Left aligned (width 5):  |{n:<5d}|")
print(f"Centered (width 5):      |{n:^5d}|")

# Binary, octal, and hexadecimal representation
print(f"Binary: {n:b}")
print(f"Octal:  {n:o}")
print(f"Hex:    {n:x}")

# -------------------------------------------------------
# 3. TEXT ALIGNMENT AND WIDTH
# -------------------------------------------------------

title = "PYTHON FORMATTING"
print(f"\n{'=' * 40}") # "=" will be printed 40 times
print(f"{title:^40}")  # center the title
print(f"{'=' * 40}\n")

items = [("Apple", 5, 0.5), ("Banana", 12, 0.2), ("Cherry", 100, 0.05)]

print(f"{'Item':<10}{'Qty':>10}{'Price':>20}")
print("-" * 40)
for item, qty, price in items:
    print(f"{item:<10}{qty:>10}{price:>20.2f}")

# -------------------------------------------------------
# 4. THOUSAND SEPARATORS AND PERCENTAGES
# -------------------------------------------------------

big_number = 1234567890
print(f"\nWith commas: {big_number:,}")
print(f"With underscores: {big_number:_}")

percentage = 0.8457
print(f"Percentage: {percentage:.2%}")  # converts 0.8457 → 84.57%

# -------------------------------------------------------
# 5. MULTILINE STRINGS AND TEMPLATES
# -------------------------------------------------------

# Triple-quoted strings can be used for clean multi-line output.
report = f"""
{'='*40}
SALES REPORT
{'='*40}
Total Items Sold: {sum(qty for _, qty, _ in items)}  # generator expression
Total Revenue:    ${sum(qty * price for _, qty, price in items):.2f}
{'='*40}
"""
print(report)

# -------------------------------------------------------
# 6. USING FORMAT SPECIFIERS WITH .format()
# -------------------------------------------------------

value = 1234.56789
print("Formatted with format(): {:10.2f}".format(value))
print("With commas: {:,}".format(value))
print("As percent: {:.1%}".format(0.253))

# -------------------------------------------------------
# 7. COLORFUL OUTPUT (Optional & Fun)
# -------------------------------------------------------

# ANSI escape codes let you colorize terminal text (no imports needed)
# Works in most terminals (not all IDEs)

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

print(f"{GREEN}Success:{RESET} Data processed correctly.")
print(f"{RED}Error:{RESET} File not found.")
print(f"{YELLOW}Warning:{RESET} Low disk space.")
print(f"{BLUE}Info:{RESET} Backup completed.")
