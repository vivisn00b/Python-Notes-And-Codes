# Recursion happens when a function calls itself to solve smaller versions of a problem.
# Every recursive function has:
# A base case → when to stop.
# A recursive case → when to keep going.
# Python limits recursion depth (default ≈ 1000).
import sys
print(sys.getrecursionlimit())

# EXAMPLE 1: SIMPLE COUNTDOWN

def countdown(n):
    if n == 0:
        print("Lift off!")
    else:
        print(n)
        countdown(n-1)  # recursive call
countdown(5)

#countdown(3) → prints 3 → calls countdown(2)
# countdown(2) → prints 2 → calls countdown(1)
# countdown(1) → prints 1 → calls countdown(0)
# countdown(0) → prints "Lift off!" → returns


# EXAMPLE 2: FACTORIAL

def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # 120

# factorial(5)
# → 5 × factorial(4)
# → 5 × 4 × factorial(3)
# → 5 × 4 × 3 × factorial(2)
# → 5 × 4 × 3 × 2 × factorial(1)
# → 5 × 4 × 3 × 2 × 1 = 120


# EXAMPLE 3: SUM OF DIGITS

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
print(sum_of_digits(1234))