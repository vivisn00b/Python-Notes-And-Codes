# Reshaping in NumPy refers to modifying the dimensions of an existing array without changing its data. The reshape() function is used for this purpose.
# It reorganizes the elements into a new shape, which is useful in machine learning, matrix operations and data preparation.

import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
r = a.reshape(2, 3)
print(r)

b = np.array([1, 2, 3, 4, 5, 6, 7, 8])
r = b.reshape(2, 2, 2)     # 3D array
print(r)

# Use -1 when one dimension is unknown. NumPy calculates that missing dimension automatically.
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
r = c.reshape(3, -1)
s = c.reshape(-1, 6)
print(r)
print(s)

# numpy.resize() function is used to change the size of an existing NumPy array.
# It modifies the array permanently and adjusts its shape to the new dimensions.
# If the new shape requires more elements than available, NumPy repeats the array elements. If less space is required, elements are truncated.

arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize((2, 3))
arr2 = np.resize(arr, (2, 2))
print(arr)
print(arr2)


rg = np.random.default_rng(1)      # NumPy random number generator
a = np.floor(10 * rg.random((3, 4)))
print(a)

print(a.ravel())     # returns the array, flattened
print(a.T)           # returns the array, transposed
print("shape of original array: ", a.shape, "\n", "shape of transposed array: ", a.T.shape)

# Stacking together different arrays
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
print(a, "\n", b)
print(np.vstack((a, b)))    # vertical stacking
print(np.hstack((a, b)))    # horizontal stacking

# column_stack function stacks 1D arrays as columns into a 2D array. It is equivalent to hstack only for 2D arrays
from numpy import newaxis
print(np.column_stack((a, b)))     # with 2D arrays
print(np.hstack((a, b)))           # same result
a = np.array([4, 2])
b = np.array([1, 0])
print(np.column_stack((a, b)))     # returns 2D array
print(np.hstack((a, b)))           # different result
print(a[:, newaxis])               # view `a` as a 2D column vector
stacked_arr = np.column_stack((a[:, newaxis], b[:, newaxis]))
stacked_arr_2 = np.hstack((a[:, newaxis], b[:, newaxis]))     # the result is the same
print(stacked_arr, "\n", stacked_arr_2)

print(np.concatenate((a, b)))      # joins two arrays
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print(np.concatenate((a, b)))
# axis=0 -> rows
print(np.concatenate((a, b), axis=0))
# axis=1 -> columns
print(np.concatenate((a, b), axis=1))

# r_ is a convenient shortcut for concatenating arrays row-wise (along axis 0)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.r_[a, b]
print(result)

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6]])
print(np.r_[a, b])       # Equivalent to: np.vstack((a, b))

# Using range and step
print(np.r_[0:10:2])
print(np.r_[1:4, 0, 4])  # creates the sequence 1, 2, 3 (the stop value 4 is excluded), then 0 and 4 are appended

# c_ is the column-wise version of r_. It concatenates arrays along axis 1 (columns) and is mainly used to quickly build 2D arrays
c = np.c_[1, 2, 3]
print(c)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.c_[a, b]      # Equivalent to: np.column_stack((a, b))

print(np.c_[0:3, 3:6])   # ranges of column

print(np.c_[a, np.full(len(a), 10)])      # mixing arrays and scalars
print(np.c_[a, [10, 10, 10]])

# Splitting one array into several smaller ones
# numpy.hsplit() performs horizontal splitting, which divides the array column-wise (axis=1)
m = np.floor(10 * rg.random((2, 12)))
print(m)
print(np.hsplit(m, 3))      # Split `a` into 3
print(np.hsplit(a, (3, 4)))      # Split `a` after the third and the fourth column

# numpy.split() is used to divide an array into equal-sized subarrays.
# The number of splits must perfectly divide the size of the array along the chosen axis.
# If equal division is not possible, NumPy will raise an error.
arr = np.arange(6)
res = np.split(arr, 2)
print(res)

# numpy.array_split() works like split(), but it allows uneven splitting.
arr = np.arange(13)
res = np.array_split(arr, 4)
print(res)

# numpy.vsplit() performs vertical splitting, meaning it divides a matrix row-wise (along axis=0).
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
res = np.vsplit(arr, 2)
print(res)

# numpy.dsplit() is used for 3D arrays. It splits the array along the third axis (axis=2).
arr = np.arange(24).reshape((2, 3, 4))
res = np.dsplit(arr, 2)
print(res)