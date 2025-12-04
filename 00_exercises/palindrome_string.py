# Task 6: Check if a string is a palindrome (ignore spaces and case)
#
# A palindrome reads the same forward and backward.
#
# Examples:
# "madam"
# "race car"
# "Level"
#
# Your program should:
#
# Take a string
#
# Remove spaces
#
# Convert everything to lowercase
#
# Check if it reads the same backwards
#
# Print “Palindrome” or “Not palindrome”
#
# Example:
# Input → "Race car"
# Output → Palindrome

text = input("Enter the string: ")
clean = ""
for char in text:
    if char != " ":
        clean += char.lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")