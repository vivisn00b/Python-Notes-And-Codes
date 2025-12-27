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


# ORDERING
# argmax, argmin, argsort, max, min, ptp, searchsorted, sort
a = np.array([40, 10, 30, 20])

# max(): Maximum value
print("max:", np.max(a))

# min(): Minimum value
print("min:", np.min(a))

# argmax(): Index of maximum value
print("argmax:", np.argmax(a))

# argmin(): Index of minimum value
print("argmin:", np.argmin(a))

# ptp(): Peak to peak (max - min)
print("ptp:", np.ptp(a))

# argsort(): Indices that would sort the array
print("argsort:", np.argsort(a))

# sort(): Sorts the array in-place
sorted_a = np.sort(a)
print("sort:", sorted_a)

# searchsorted(): Index to insert element to keep array sorted
print("searchsorted (25):", np.searchsorted(sorted_a, 25))


# OPERATIONS
# choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask, real, sum
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
cond = np.array([True, False, True, False])

# choose(): Select elements based on index array
choices = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])
index = np.array([0, 1, 0, 1])
print("choose:", np.choose(index, choices))

# compress(): Select elements where condition is True
print("compress:", np.compress(cond, a))

# cumsum(): Cumulative sum
print("cumsum:", np.cumsum(a))

# cumprod(): Cumulative product
print("cumprod:", np.cumprod(a))

# inner(): Inner product of arrays
print("inner:", np.inner(a, b))

# ndarray.fill(): Fill array with a value
x = np.empty(4)
x.fill(5)
print("fill:", x)

# Complex number operations
c = np.array([1+2j, 3+4j])
print("real:", c.real)
print("imag:", c.imag)

# prod(): Product of elements
print("prod:", np.prod(a))

# put(): Replace elements at given indices
d = a.copy()
np.put(d, [0, 2], [100, 200])
print("put:", d)

# putmask(): Replace elements where condition is True
e = a.copy()
np.putmask(e, e > 2, 99)
print("putmask:", e)

# sum(): Sum of elements
print("sum:", np.sum(a))


# BASIC LINEAR ALGEBRA
# cross, dot, outer, linalg.svd, vdot
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# cross(): Cross product of vectors
print("cross:", np.cross(a, b))

# dot(): Dot product
print("dot:", np.dot(a, b))

# outer(): Outer product
print("outer:\n", np.outer(a, b))

# vdot(): Vector dot product (handles complex numbers)
c = np.array([1+2j, 3+4j])
d = np.array([5+6j, 7+8j])
print("vdot:", np.vdot(c, d))

# linalg.svd(): Singular Value Decomposition
M = np.array([[1, 2], [3, 4]])
U, S, Vt = np.linalg.svd(M)
print("SVD U:\n", U)
print("SVD S:\n", S)
print("SVD Vt:\n", Vt)
