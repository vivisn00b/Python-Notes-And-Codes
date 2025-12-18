import numpy as np

# CREATING ARRAYS:
a = np.array([2, 3, 4])
print(a)
print(a.dtype.name)
b= np.array([1.1, 2.2, 3.3, 5., 4])
print(b)
print(b.dtype)    # "float64" as numpy arrays are homogeneous
c = np.array([(1.5,2,3), (4,5,6)])
print(c.shape)
print(c.ndim)
print(c.dtype)
print(c.size)
print(c.itemsize)
print(type(c))   # numpy.ndarray
print(c.data)    # the buffer containing the actual elements of the array

# The type of the array can also be explicitly specified at creation time:
c = np.array([ [1,2], [3,4] ], dtype=complex)
print(c)

# Array creation using functions
# zeros creates an array full of zeros; by default, the dtype of the created array is float64
print(np.zeros((3, 4)))   # 3 rows, 4 columns

# ones creates an array full of ones
print(np.ones((2, 3, 4), dtype = np.int16))    # creates 2 3x4 arrays with specific dtype

# empty creates an array whose initial content is random and depends on the state of the memory
print(np.empty((2, 3)))    # uninitialized, output may vary

# To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists
d = np.arange(10, 30, 5)
print(d)
e = np.arange(0, 2, 0.5)
print(e)

# When arange is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision.
# For this reason, it is usually better to use the function linspace that receives as an argument the number of elements that we want, instead of the step
f = np.linspace(0, 2, 9)      # 9 numbers from 0 to 2
print(f)
from numpy import pi
f = np.linspace(0, 2*pi, 10)
print(f)
x = np.sin(f)
print(f)


# PRINTING ARRAYS:
g = np.arange(24).reshape(2, 3, 4)      # prints 2 3x4 arrays
print(g)