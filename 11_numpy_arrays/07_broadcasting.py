# Broadcasting lets NumPy perform operations on arrays of different shapes without writing loops.
import numpy as np

arr = np.array([10, 20, 30])
arr + 5
print(arr)

# Broadcasting Rules (MOST IMPORTANT)
# NumPy compares shapes from right to left.
# Two dimensions are compatible if: they are equal, OR one of them is 1
# If neither is true → ERROR.

# 1D → 2D
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])
print(A + B)

# Row-wise Broadcasting
A = np.array([[1, 2, 3],
              [4, 5, 6]])
row = np.array([10, 20, 30])
print(A + row)

# Column-wise Broadcasting
col = np.array([[10],
                [20]])
print(A + col)

# Reshaping to Force Broadcasting
v = np.array([10, 20])
v.reshape(2, 1)
#v[:, np.newaxis]

# example:
print(A + v[:, None])

# Broadcasting with Different Dimensions
A = np.ones((3, 4, 5))
B = np.ones((5,))
print(A, "\n", B)

A = np.ones((3, 2))     # 3x2 array
B = np.ones((3,))       # 3x1 array
#A + B                  # Error as there are only 2 columns in A and 3 in B
#print(B[:, None])      # gives column vector; np.newaxis can also be used
print(A + B[:, None])   # Fix

# Broadcasting in Higher Dimensions
A = np.ones((3, 4, 5))
B = np.array([1, 2, 3, 4, 5])
C = A + B
print(C.shape, "\n", C)

# Broadcasting with NumPy Functions
A = np.array([[1, 4, 9],
              [16, 25, 36]])
print(np.sqrt(A))
A = np.array([1, 5, 10])
print(np.maximum(A, 6))
A = np.array([1, 2, 3, 4])
print(np.where(A > 2, 1, 0))

# Real Data Analytics Use Case: Feature Scaling
X = np.array([[50, 100],
              [60, 120],
              [55, 110]])
mean = X.mean(axis=0)
std = X.std(axis=0)
X_scaled = (X - mean) / std
print(X_scaled)
