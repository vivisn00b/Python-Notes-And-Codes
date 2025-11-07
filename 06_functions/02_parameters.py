# -------------------------------------------------------
# 1. POSITIONAL PARAMETERS
# -------------------------------------------------------

def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person("Vivek", 24)     # order matters
describe_person(24, "Vivek")     # this makes no sense logically but Python will still run it


# -------------------------------------------------------
# 2. KEYWORD ARGUMENTS
# -------------------------------------------------------

describe_person(age=30, name="Aditi")  # order doesn't matter now


# -------------------------------------------------------
# 3. DEFAULT PARAMETERS
# -------------------------------------------------------

def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user("Ravi")
greet_user()  # uses default


# -------------------------------------------------------
# 4. *ARGS → VARIABLE POSITIONAL ARGUMENTS
# -------------------------------------------------------

def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum:", sum_all(1, 2, 3))
print("Sum:", sum_all(10, 20, 30, 40))


# -------------------------------------------------------
# 5. **KWARGS → VARIABLE KEYWORD ARGUMENTS
# -------------------------------------------------------

def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_profile(name="Vivek", role="Engineer", city="Kolkata")


# -------------------------------------------------------
# 6. COMBINING ALL TOGETHER
# -------------------------------------------------------

def user_info(name, *hobbies, **details):
    print(f"Name: {name}")
    if hobbies:
        print("Hobbies:", ", ".join(hobbies))
    for key, value in details.items():
        print(f"{key}: {value}")

user_info("Vivek", "Coding", "Gaming", city="Bangalore", role="System Engineer")
