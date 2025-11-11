# --------------------------------------------------
# Python Error Handling — try, except, else, finally
# --------------------------------------------------

# 1 Basic try-except
print("Basic try-except:")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can’t divide by zero!")
print("-" * 50)


# 2 Multiple Exception Types
print("Multiple Exception Types:")

try:
    num = int("abc")  # ValueError
except ValueError:
    print("That’s not a number!")
except TypeError:
    print("Type mismatch error!")
print("-" * 50)


# 3 Catching Multiple Exceptions in One Block
print("Multiple Exceptions, One Block:")

try:
    items = [1, 2, 3]
    print(items[5])  # IndexError
except (ValueError, IndexError) as e:
    print("Caught error:", e)
print("-" * 50)


# 4 Using else (runs when no exception occurs)
print("try–except–else:")

try:
    n = int("42")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful:", n)
print("-" * 50)


# 5 Using finally (always runs)
print("try–except–finally:")

try:
    file = open("sample.txt", "w")
    file.write("Testing finally block!")
except OSError as e:
    print("File error:", e)
finally:
    file.close()
    print("File closed (finally always executes).")
print("-" * 50)


# 6 Raising Exceptions Manually
print("Raising Exceptions:")

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero!")
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print("Manual exception:", e)
print("-" * 50)


# 7 Custom Exception Classes
print("Custom Exception Classes:")

class NegativeNumberError(Exception):
    """Raised when a number is negative."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Negative number not allowed!")
    return x ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Custom error caught:", e)
print("-" * 50)


# Mini Exercise
print("Mini Exercise:")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Both inputs must be numbers!"
    finally:
        print("Operation attempted.")

print(safe_divide(10, 2))
print(safe_divide(5, 0))
print(safe_divide("x", 3))
print("-" * 50)
