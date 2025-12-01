# Task 1: Count the vowels
#
# Write a Python program that:
#
# Takes a sentence as input
#
# Counts how many vowels are in it (a, e, i, o, u — both uppercase and lowercase)
#
# Prints the total count
#
# Try to do it using a loop — don’t use fancy shortcuts yet.
#
# Example:
# Input → "Hello World"
# Output → 3

print("Vowel counting operation")
str = input("Enter the sentence: ")
l = len(str)
count = 0
for i in range(0, l):
    c = str[i]
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        count += 1
print(count)


# More precise, python like version:
text = input("Enter the sentence: ")
count = 0
for char in text:
    if char in "aeiouAEIOU":
        count += 1
print(count)
