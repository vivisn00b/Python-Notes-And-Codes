# Task 8: Count how many times each word appears in a sentence
#
# Example input:
# "cat dog cat mouse dog cat"
#
# Expected output:
#
# cat: 3
# dog: 2
# mouse: 1

text = input("Enter the string:")
text_list = text.split()
word_dict = {}
for word in text_list:
    if word in list(word_dict.keys()):
        word_dict[word] = word_dict.get(word) + 1
    else:
        word_dict[word] = 1
print(word_dict)

# Cleaner version:
text = input("Enter the string: ")
text_list = text.split()
word_dict = {}
for word in text_list:
    if word in word_dict:
        word_dict[word] = word_dict.get(word) + 1
    else:
        word_dict[word] = 1
print(word_dict)
