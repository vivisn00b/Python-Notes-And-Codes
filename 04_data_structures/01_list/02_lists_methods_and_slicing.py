# 02_lists_methods_and_slicing.py
# --------------------------------------------------
# Python List Methods & Advanced Slicing
# --------------------------------------------------

# Base list for experiments
nums = [5, 2, 9, 1, 5, 6]
print("Original list:", nums)
print("-" * 50)


# 1 Common List Methods
print("Common List Methods:")

nums.append(10)                # add one item to the end
print("append(10):", nums)

nums.extend([11, 12])          # add multiple items
print("extend([11, 12]):", nums)

nums.insert(2, 100)            # insert at specific index
print("insert(2, 100):", nums)

nums.remove(5)                 # removes first occurrence of 5
print("remove(5):", nums)

popped = nums.pop()            # removes last element and returns it
print("pop() removed:", popped, " →", nums)

nums.sort()                    # sorts in place
print("sort():", nums)

nums.reverse()                 # reverses in place
print("reverse():", nums)

nums.clear()                   # empties list
print("clear():", nums)
print("-" * 50)


# 2 Re-create list for slicing examples
nums = [10, 20, 30, 40, 50, 60, 70]
print("Slicing Examples:")
print("Full list:", nums)

print("nums[0:3] →", nums[0:3])     # first 3 elements
print("nums[:4]  →", nums[:4])      # shorthand start
print("nums[3:]  →", nums[3:])      # shorthand end
print("nums[-3:] →", nums[-3:])     # last 3 elements
print("nums[::2] →", nums[::2])     # every 2nd element
print("nums[::-1]→", nums[::-1])    # reversed list
print("-" * 50)


# 3 Nested List Access
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Nested List Access:")
print("Row 0:", matrix[0])
print("matrix[1][2] →", matrix[1][2])  # row 1, column 2

# flattening using list comprehension
flat = [num for row in matrix for num in row]
print("Flattened list:", flat)
print("-" * 50)


# 4 Copying and Comparing Lists
a = [1, 2, 3]
b = a.copy()
c = a
a.append(4)
print("Copying & Comparing:")
print("a:", a)
print("b (copy):", b)
print("c (same ref):", c)
print("a == b ?", a == b)     # compares values
print("a is b ?", a is b)     # compares identity
print("-" * 50)


# 5 Membership & Counting
nums = [1, 2, 2, 3, 4, 2]
print("Membership & Counting:")
print("2 in nums ?", 2 in nums)
print("nums.count(2):", nums.count(2))
print("nums.index(3):", nums.index(3))   # first occurrence of 3
print("-" * 50)


# Predict: what will be printed?
letters = ["a", "b", "c", "d", "e", "f"]
print("Mini Exercise:")
print("letters[1:5:2] →", letters[1:5:2])   # step of 2 within slice
print("letters[::-2] →", letters[::-2])     # reverse with step
print("letters[::3]  →", letters[::3])
print("-" * 50)
