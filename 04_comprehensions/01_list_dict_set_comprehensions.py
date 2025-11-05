# -------------------------------------------------------
# 1. LIST COMPREHENSIONS — transform and filter lists
# -------------------------------------------------------

# Traditional way
squares = []
for x in range(1, 6):
    squares.append(x**2)
print("Squares (loop): ", squares)

# Comprehension way
squares_comp = [x**2 for x in range(1,6)]
print("Squares (comprehension): ", squares)

# Add filtering
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# Nested loops inside comprehension
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]] # list of tuples
print("Pairs:", pairs)
pairs[0]
print(pairs[0][1])  # → 4   (the y value of first pair)

# Conditional expression inside comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]
print("Labels:", labels)

# -------------------------------------------------------
# 2. DICTIONARY COMPREHENSIONS
# -------------------------------------------------------

# Square mapping
square_map = {x: x**2 for x in range(1,6)}
print("Square map:", square_map)

# Filtered dictionary
filtered_map = {k: v for k, v in square_map.items() if v > 10}
print("Filtered map:", filtered_map)

# Reverse key-value pairs
reversed_map = {v: k for k, v in square_map.items()}
print("Reversed map:", reversed_map)

# -------------------------------------------------------
# 3. SET COMPREHENSIONS — unique filtered data
# -------------------------------------------------------

nums = [1, 2, 2, 3, 3, 4, 5]
unique_squares = {x ** 2 for x in nums}
print("Unique squares (set):", unique_squares)

# -------------------------------------------------------
# 4. GENERATOR EXPRESSIONS — lazy comprehensions
# -------------------------------------------------------

# Use parentheses instead of brackets
gen = (x ** 2 for x in range(1, 6))
print("Generator object:", gen)

# You can iterate over it once
for val in gen:
    print("Generated:", val)

# -------------------------------------------------------
# WORD LENGTH FILTER
# -------------------------------------------------------

sentence = "I am currently learning Python for data analysis"
words = sentence.split()
word_lengths = {word: len(word) for word in words if len(word) > 3}
print("Word lengths (dict): ", word_lengths)

acronym = "".join(word[0].upper() for word in words)
print("Acronym: ", acronym)