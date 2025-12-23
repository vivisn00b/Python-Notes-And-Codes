# ARRAY CREATION
# arange, array, copy, empty, empty_like, eye, fromfile, fromfunction, identity,
# linspace, logspace, mgrid, ogrid, ones, ones_like, r_, zeros, zeros_like

import numpy as np
# -------------------------------
# Basic creation
# -------------------------------
a = np.array([1, 2, 3])
b = np.copy(a)

# -------------------------------
# Zeros / Ones / Empty
# -------------------------------
z = np.zeros((2, 3))
o = np.ones((2, 3))
e = np.empty((2, 3))

z_like = np.zeros_like(a)
o_like = np.ones_like(a)
e_like = np.empty_like(a)

# -------------------------------
# Ranges & sequences
# -------------------------------
ar = np.arange(0, 10, 2)
ls = np.linspace(0, 1, 5)
lg = np.logspace(1, 3, 3)

# -------------------------------
# Identity / Diagonal matrices
# -------------------------------
eye_m = np.eye(3)
id_m = np.identity(4)
# -------------------------------
# Grid creation
# -------------------------------
mg = np.mgrid[0:3, 0:3]
og = np.ogrid[0:3, 0:3]

# -------------------------------
# From function / file
# -------------------------------
ff = np.fromfunction(lambda i, j: i + j, (3, 3))

# (Example – requires existing binary file)
# ff_file = np.fromfile("data.bin", dtype=np.float32)

# -------------------------------
# Special constructors
# -------------------------------
r = np.r_[1:5]

# -------------------------------
# Print all (optional)
# -------------------------------
print(
    a, b, z, o, e,
    z_like, o_like, e_like,
    ar, ls, lg,
    eye_m, id_m,
    mg, og,
    ff, r,
    sep="\n\n"
)

# Conversions
# ndarray.astype, atleast_1d, atleast_2d, atleast_3d, asmatrix
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

# -------------------------------
# astype (change data type)
# -------------------------------
a_float = a.astype(float)
a_str = a.astype(str)

# -------------------------------
# atleast_1d
# -------------------------------
at1_scalar = np.atleast_1d(5)
at1_array = np.atleast_1d(a)

# -------------------------------
# atleast_2d
# -------------------------------
at2_scalar = np.atleast_2d(5)
at2_array = np.atleast_2d(a)
at2_matrix = np.atleast_2d(b)

# -------------------------------
# atleast_3d
# -------------------------------
at3_scalar = np.atleast_3d(5)
at3_array = np.atleast_3d(a)
at3_matrix = np.atleast_3d(b)

# -------------------------------
# mat (convert to matrix class)
# -------------------------------
m1 = np.asmatrix(a)
m2 = np.asmatrix(b)
m3 = np.asmatrix("1 2; 3 4")

# -------------------------------
# Print all (optional)
# -------------------------------
print(
    a_float, a_str,
    at1_scalar, at1_array,
    at2_scalar, at2_array, at2_matrix,
    at3_scalar, at3_array, at3_matrix,
    m1, m2, m3,
    sep="\n\n"
)