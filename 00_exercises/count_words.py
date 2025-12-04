# Task 7: Count words in a sentence
#
# Write a program that:
#
# Takes a sentence (string)
#
# Counts how many words it has
#
# Words are separated by spaces
#
# Ignore extra spaces (e.g., " Python is fun " should still count correctly as 3)
#
# Expected behavior:
# Input → "Python is fun"
# Output → 3
from itertools import count

text = input("Enter the string: ")
text_list = text.split()
count = 0
for words in text_list:
    count += 1
print(count)

# Shorter version:
text = input("Enter the string: ")
count = len(text.split())
print(count)