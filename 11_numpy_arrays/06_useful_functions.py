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

print(
    a, b, z, o, e,
    z_like, o_like, e_like,
    ar, ls, lg,
    eye_m, id_m,
    mg, og,
    ff, r,
    sep="\n\n"
)

# CONVERSIONS
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

print(
    a_float, a_str,
    at1_scalar, at1_array,
    at2_scalar, at2_array, at2_matrix,
    at3_scalar, at3_array, at3_matrix,
    m1, m2, m3,
    sep="\n\n"
)

# MANIPULATIONS
# array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit, hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes, take, transpose, vsplit, vstack
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.array([9, 10])

# -------------------------------
# JOINING / STACKING OPERATIONS
# -------------------------------

# concatenate(): Joins arrays along an existing axis
print("concatenate:\n", np.concatenate((a, b), axis=0))

# hstack(): Stacks arrays horizontally (column-wise)
print("hstack:\n", np.hstack((a, b)))

# vstack(): Stacks arrays vertically (row-wise)
print("vstack:\n", np.vstack((a, b)))

# dstack(): Stacks arrays along depth (3rd axis)
print("dstack:\n", np.dstack((a, b)))

# column_stack(): Stacks 1D arrays as columns into a 2D array
print("column_stack:\n", np.column_stack((c, c)))

# -------------------------------
# SPLITTING OPERATIONS
# -------------------------------

# array_split(): Splits array into sub-arrays (unequal split allowed)
print("array_split:", np.array_split(c, 2))

# hsplit(): Splits array horizontally
print("hsplit:", np.hsplit(a, 2))

# vsplit(): Splits array vertically
print("vsplit:", np.vsplit(a, 2))

# -------------------------------
# SHAPE MANIPULATION
# -------------------------------

# reshape(): Changes shape without changing data
print("reshape:\n", a.reshape(4, 1))

# ravel(): Flattens array into 1D (returns view if possible)
print("ravel:", a.ravel())

# squeeze(): Removes axes of length 1
print("squeeze:", np.squeeze(np.array([[[1, 2, 3]]])))

# transpose(): Swaps rows and columns
print("transpose:\n", a.transpose())

# swapaxes(): Swaps any two axes
print("swapaxes:\n", np.swapaxes(a, 0, 1))

# -------------------------------
# SIZE MODIFICATION
# -------------------------------

# repeat(): Repeats elements of an array
print("repeat:", np.repeat(c, 2))

# resize(): Resizes array (repeats data if new size is larger)
print("resize:\n", np.resize(c, (3, 3)))

# -------------------------------
# INDEXING / SELECTION
# -------------------------------

# take(): Takes elements from array using indices
print("take:", np.take(c, [0, 1]))

# diagonal(): Returns diagonal elements of array
print("diagonal:", np.diagonal(a))

# ndarray.item(): Returns Python scalar from array
print("item:", c.item(0))

# -------------------------------
# DIMENSION EXPANSION
# -------------------------------

# newaxis: Adds a new dimension to array
print("newaxis:\n", c[:, np.newaxis])

# QUESTIONS
# all, any, nonzero, where
a = np.array([1, 0, 3, 0, 5])

# all(): True if all elements are non-zero / True
print("all:", np.all(a))

# any(): True if at least one element is non-zero / True
print("any:", np.any(a))

# nonzero(): Returns indices of non-zero elements
print("nonzero:", np.nonzero(a))

# where(): Returns indices where condition is True
print("where a > 2:", np.where(a > 2))

# where() with condition (ternary operation)
b = np.where(a > 2, a, 0)
print("where condition result:", b)
