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

# MASKING: filtering data using conditions, without loops.
arr = np.array([10, 25, 40, 55, 70])
mask = arr > 40
print(mask)

high_values = arr > 40     # save the mask (best practice)
arr[high_values]

print(arr[(arr > 20) & (arr < 60)])    # multiple conditions

# masking with NaNs (real ETL case)
arr = np.array([10, np.nan, 30, np.nan, 50])
clean = arr[~np.isnan(arr)]
print(clean)

# replace values using masking
arr = np.array([100, 200, 300, 400])
arr[arr > 250] = 250
print(arr)

# masking in 2D arrays
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(data[data > 50])
# output: [60 70 80 90]: masking flattens the result by default

# row-wise filtering (ETL-style)
# example: keep rows where column 1 > 50
print(data[data[:, 1] > 50])

# EXTRAS
rg = np.random.default_rng(1)     # create instance of default random number generator
a = np.ones((2, 3), dtype = int)
b = rg.random((2, 3))
print(a, "\n", b)
#a += b     # error because datatype of arrays are different

c = np.exp(a * 1j)
print(c)
print(c.dtype)

print(a.sum(axis=0))     # sum of each column
print(b.min(axis=1))     # min of each row
print(a.cumsum(axis=1))  # cumulative sum along each row

X = np.arange(3)
print(X)
print(np.exp(X))
print(np.sqrt(X))