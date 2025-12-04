# Task 9: Remove duplicates while keeping original order
# Problem:
# You’re given a list like:
# [3, 1, 3, 2, 5, 3, 2, 1]
#
# Create a new list that contains each number only once, but in the same order they first appeared.
# Expected Output:
# [3, 1, 2, 5]
#
# Conditions:
# • Use a loop
# • Use an empty list
# • Use an if condition
# • Do NOT use set(), sorting, or shortcuts like dict.fromkeys

og_list = [3, 1, 3, 2, 5, 3, 2, 1]
new_list = []
for num in og_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)