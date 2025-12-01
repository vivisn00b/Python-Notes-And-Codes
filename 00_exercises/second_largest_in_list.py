# Task 2: Second largest number in a list (without using sort())
#
# Write a program that:
#
# Takes a list of numbers (you can hardcode something like [3, 8, 1, 9, 4])
#
# Finds the second largest number
#
# Does not use sort() or sorted()
#
# Hint:
# Track the largest and second largest as you iterate.
#
# Example:
# List → [3, 8, 1, 9, 4]
# Output → 8

list = [3, 8, 1, 9, 4]
min = 0
max = 0
for i in list:
    if max < i:
        min = max
        max = i
print("Largest: ", max)
print("Second largest: ", min)

# More robust version
nums = [3, 8, 1, 9, 4]
largest = float("-inf")        # negative infinity
second_largest = float("-inf")

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n
print("Largest:", largest)
print("Second largest:", second_largest)
