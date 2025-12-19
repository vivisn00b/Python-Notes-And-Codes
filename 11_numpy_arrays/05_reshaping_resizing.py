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
print(r)