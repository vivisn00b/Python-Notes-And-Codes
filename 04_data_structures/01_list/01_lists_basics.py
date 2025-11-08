# Lists can contain any type.
# They are ordered — elements maintain the order you insert them.
# They are mutable — you can change their contents in place.

# --------------------------------------------------
# Python Lists — Ordered, Mutable Collections
# --------------------------------------------------

# 1 Creating Lists
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [1, [2, 3], [4, [5, 6]]]

print("Creating Lists:")
print(numbers)
print(mixed)
print(nested)
print("-" * 50)

# Creating List with Repeated Elements
a = [2] * 5
b = [0] * 7
print(a)
print(b)

#  Using list() Constructor
# We can also create a list by passing an iterable (like a tuple, string or another list) to the list() function.
a = list((1, 2, 3, 'apple', 4.5))
print(a)


# 2 Accessing Elements
nums = [10, 20, 30, 40, 50]
print("Accessing Elements:")
print(nums[0])      # first element
print(nums[-1])     # last element
print(nums[1:4])    # slicing (20, 30, 40)
print("-" * 50)


# 3 Modifying Lists
nums = [1, 2, 3, 4, 5]
nums[0] = 100
nums.append(6)           # add at end
nums.insert(2, 999)      # insert at index 2
nums.remove(3)           # remove first occurrence of 3
del nums[-1]             # delete by index (last element)
print("Modifying Lists:")
print(nums)
print("-" * 50)


# 4 Iterating Through Lists
nums = [10, 20, 30]
print("Iterating Through Lists:")
for n in nums:
    print(n)

for i, val in enumerate(nums):
    print(f"Index {i} → {val}")
print("-" * 50)


# 5 Combining Lists
a = [1, 2, 3]
b = [4, 5]
combined = a + b            # creates new list
a.extend(b)                 # modifies existing list
print("Combining Lists:")
print("combined:", combined)
print("a after extend:", a)
print("-" * 50)


# 6 List Functions and Operations
nums = [3, 1, 4, 2, 5]
print("Built-in List Functions:")
print("len:", len(nums))
print("max:", max(nums))
print("min:", min(nums))
print("sum:", sum(nums))
print("sorted:", sorted(nums))
print("-" * 50)


# 7 Copying Lists — reference vs actual copy
nums = [1, 2, 3]
copy1 = nums          # same reference
copy2 = nums.copy()   # new list
nums.append(4)
print("Copying Lists:")
print("original nums:", nums)
print("copy1 (same reference):", copy1)
print("copy2 (independent):", copy2)
print("-" * 50)


# Predict before running
data = [1, 2, 3]
x = data
y = data[:]           # shallow copy
x.append(4)
y.append(5)
print("Output:")
print("data:", data)
print("x:", x)
print("y:", y)
print("-" * 50)
