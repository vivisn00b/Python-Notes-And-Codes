# Task 3: Reverse each word but keep the sentence order
#
# Write a program that:
#
# Input:
# "Python is fun"
#
# Output:
# "nohtyP si nuf"
#
# Rules:
# • Do not reverse the whole sentence.
# • Reverse each word separately.
# • Keep the words in their original positions.

str = "Python is fun"
rev = ""
for word in str.split():
    rev += word[::-1]
    rev += " "
print(rev)

# More polished
text = "Python is fun"
rev = ""

for word in text.split():
    rev += word[::-1] + " "

rev = rev.strip()   # remove the last space
print(rev)