# --------------------------------------------------
# Python Strings — Immutable Sequences of Characters
# --------------------------------------------------

# 1 Creating Strings
print("Creating Strings:")

single = 'Hello'
double = "World"
multiline = """This
is
a multiline string."""
print(single)
print(double)
print(multiline)
print("-" * 50)


# 2 String Indexing and Slicing
print("Indexing and Slicing:")

text = "Python"
print("text[0] →", text[0])      # first char
print("text[-1] →", text[-1])    # last char
print("text[1:4] →", text[1:4])  # slicing (excludes end)
print("text[:3] →", text[:3])    # from start to index 2
print("text[::2] →", text[::2])  # every 2nd character
print("Reversed:", text[::-1])
print("-" * 50)


# 3 String Immutability
print("String Immutability:")

word = "Python"
try:
    word[0] = "J"
except TypeError as e:
    print("Error:", e)
word = "J" + word[1:]
print("Modified word (new string):", word)
print("-" * 50)


# 4 Common String Methods
print("Common String Methods:")

msg = "  hello, python!  "
print("Uppercase:", msg.upper())
print("Lowercase:", msg.lower())
print("Title Case:", msg.title())
print("Stripped:", msg.strip())
print("Replace:", msg.replace("python", "world"))
print("Split:", msg.split(","))
print("Joined:", "-".join(["one", "two", "three"]))
print("Count of 'l':", msg.count("l"))
print("Startswith 'h':", msg.startswith("h"))
print("Endswith '!':", msg.endswith("!"))
print("-" * 50)


# 5 String Searching
print("String Searching:")

quote = "Knowledge is power, but enthusiasm pulls the switch."
print("Find 'power' at index:", quote.find("power"))
print("Contains 'wisdom'?", "wisdom" in quote)
print("Contains 'power'?", "power" in quote)
print("-" * 50)


# 6 String Formatting
print("String Formatting:")

name = "Alice"
age = 25
print("Using f-string:", f"{name} is {age} years old.")
print("Using format():", "{} is {} years old.".format(name, age))
print("Using % operator: %s is %d years old." % (name, age))
print("-" * 50)


# 7 Escape Sequences
print("Escape Sequences:")

print("Newline:\nSecond line")
print("Tab:\tIndented text")
print("Quote inside string: \"Python\" is fun")
print("Backslash: C:\\Users\\Name")
print("-" * 50)


# 8 Iterating and Checking Characters
print("Iterating and Checking Characters:")

sample = "AbC123"
for ch in sample:
    print(ch, "→",
          "digit" if ch.isdigit() else
          "alpha" if ch.isalpha() else
          "other")

print("Is all alpha?", sample.isalpha())
print("Is all digit?", sample.isdigit())
print("Is alphanumeric?", sample.isalnum())
print("-" * 50)


# Mini Exercise
print("Mini Exercise:")

sentence = "the quick brown fox jumps over the lazy dog"
# Capitalize every word and count vowels
capitalized = sentence.title()
vowels = sum(1 for ch in sentence if ch.lower() in "aeiou")
print("Capitalized:", capitalized)
print("Total vowels:", vowels)
print("-" * 50)
