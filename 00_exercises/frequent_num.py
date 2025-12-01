# Task 4: Find the most frequent number in a list
#
# Create a Python program that:
#
# Takes a list like [3, 1, 3, 2, 5, 3, 2, 1]
#
# Counts how many times each number appears
#
# Prints the number that appears the most
#
# Do not use collections.Counter

nums = [3, 1, 3, 2, 5, 3, 2, 1]

max_count = 0
max_value = None

for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1

    if count > max_count:
        max_count = count
        max_value = i

print("Most frequent number:", max_value)
