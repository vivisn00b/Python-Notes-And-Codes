# Arithmetic operators on arrays apply elementwise

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 3], [2, 1]])

flag = a > 3     # checks if all the elements are >3
print(flag)      # returns matrix in boolean type

# Matrix product
print(a * b)     # element wise product
print(a @ b)     # matrix product
print(a.dot(b))  # another matrix product

# Adding 1 to every element
print("Adding 1 to every element:", a + 1)

# Subtracting 2 from each element
print("\nSubtracting 2 from each element:", b - 2)

# sum of array elements
# Performing Unary operations
print("\nSum of all array elements: ", a.sum())

# Adding two arrays
# Performing Binary operations
print("\nArray sum:\n", a + b)
# Addition of two Arrays
Sum = np.add(a, b)
print(Sum)

# Square root of Array
Sqrt = np.sqrt(b)
print(Sqrt)

# Transpose of Array
Trans_arr = a.T
print(Trans_arr)

# Operations on array element
arr = np.array([1, 2, 3, 4])
print(arr * 10)
print(arr + 5)
print(arr ** 2)

a = np.array([-3, -1, 0, 1, 3]) # array with both positive and negative values

# Applying a unary operation: absolute value
print(np.absolute(a))

# Mathematical operations
# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print(np.sin(a))

# exponential values
b = np.array([0, 1, 2, 3])
print(np.exp(b))
print(np.sqrt(b))

# square root of array values
print (np.sqrt(a))


# NumPy sorting arrays
dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals  = [('Hrithik', 2009, 8.5),
         ('Ajay',    2008, 8.7),
         ('Pankaj',  2008, 7.9),
         ('Aakash',  2009, 9.0)]

a = np.array(vals, dtype=dtype)

print(np.sort(a, order='name'))
print(np.sort(a, order=['year', 'cgpa']))