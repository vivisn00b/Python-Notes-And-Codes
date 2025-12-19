import numpy as np

a = np.arange(10) ** 3
print(a)
print(a[2])     # indexing
print(a[2:5])   # slicing

# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000
print(a)
print(a[::-1])     # reversed array

def f(x, y):
    return 10 * x + y
b = np.fromfunction(f, (5, 4), dtype = int)
print(b)
print(b[2, 3])    # indexing in multidimensional array
print(b[0:5, 1])  # each row in the second column of b
print(b[:, 1])    # equivalent to the previous example
print(b[1:3, :])  # each column in the second and third row of b
print(b[-1])      # the last row. Equivalent to b[-1, :]

c = np.array([[[0, 1, 2],
               [10, 12 ,13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(c.shape)    # 3D array (two stacked 2D arrays)
# For 3D array: matrix[depth, row, column]
print(c[1, ...])  # same as c[1, :, :] or c[1]
print(c[..., 2])  # same as c[:, :, 2]

# to perform an operation on each element in the array, use the flat attribute which is an iterator over all the elements of the array
for element in c.flat:
    print(element)

# Boolean indexing
arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 15])

# Fancy indexing / Advance indexing: access elements of an array by using another array or list of indices
indices = [0, 2, 4]
print(arr[indices])

# Integer array indexing: similar to fancy indexing, this method allows us to access elements at specific, non-adjacent positions which makes it useful for extracting scattered data points.
print(arr[[1, 2, 3]])

# Ellipsis (...) in Indexing: ellipsis (...) can be used to select all dimensions which are not explicitly mentioned
cube = np.random.rand(4, 4, 4)
print(cube)
print(cube[..., 0])

# using np.newaxis to Add New Dimensions
# np.newaxis keyword adds a new axis to the array which helps in converting a 1D array into a row or column vector
array = np.array([1, 2, 3])
print(array[:, np.newaxis])

# Modifying Array Elements
arr = np.array([1, 2, 3, 4])
arr[1:3] = 99
print(arr)