# -------------------------------------------------------
# 1. DEFINING AND CALLING A FUNCTION
# -------------------------------------------------------

def greet():
    print("Hello, welcome to Python functions!")

# Call the function
greet()


# -------------------------------------------------------
# 2. FUNCTIONS WITH PARAMETERS
# -------------------------------------------------------

def greet_user(name):
    print(f"Hello, {name}! Glad to have you here.")

greet_user("Vivek")
greet_user("Aditi")


# -------------------------------------------------------
# 3. FUNCTIONS THAT RETURN VALUES
# -------------------------------------------------------

def add(a, b):
    return a + b

result = add(5, 7)
print("Addition result:", result)


# -------------------------------------------------------
# 4. MULTIPLE RETURN VALUES
# -------------------------------------------------------

def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [4, 7, 2, 9, 5]
minimum, maximum = get_min_max(nums)
print(f"Min: {minimum}, Max: {maximum}")


# -------------------------------------------------------
# 5. RETURNING EARLY
# -------------------------------------------------------

def check_even(num):
    if num % 2 != 0:
        return "Odd number"
    return "Even number"

print(check_even(4))
print(check_even(7))


# -------------------------------------------------------
# 6. NESTED FUNCTIONS
# -------------------------------------------------------

def outer():
    def inner():
        print("Inner function called!")
    print("Outer function called!")
    inner()

outer()
