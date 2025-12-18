# Numpy is a general-purpose array-processing package.
# It gives vectorized operations, meaning operations happen on entire arrays at once without Python loops.
# It provides a high-performance multidimensional array object, and tools for working with these arrays.
# In Numpy, number of dimensions of the array is called rank of the array.
# A tuple of integers giving the size of the array along each dimension is known as shape of the array.
# An array class in Numpy is called as ndarray.

import numpy as np

# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print(arr)
print(type(arr))

# Creating a rank 2 Array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
print(type(arr))

# Creating an array from tuple
arr = np.array((1, 3, 2))
print(arr)
print(type(arr))

# Accessing the array Index
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Printing a range of Array
# with the use of slicing method
arr2 = arr[:2, ::2]
print("first 2 rows and alternate columns(0 and 2):\n", arr2)

# Printing elements at specific Indices
arr3 = arr[[1, 1, 0, 3],      # first list gives the row indices
[3, 2, 1, 0]]      # second list gives the column indices
print("\nElements at indices (1, 3), (1, 2), (0, 1), (3, 0):", arr3)


# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("1D array:", arr1)
print("2D array:\n", arr2)
print("Datatype:", arr1.dtype)
print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size (total no of elements):", arr2.size)
print("Size of each element:", arr2.itemsize)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]
np_arr = np.array([list1, list2, list3])
print(np_arr)
print("Array shape: ", np_arr.shape)