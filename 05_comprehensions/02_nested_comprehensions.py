# -------------------------------------------------------
# 1. BUILD A 2D MATRIX
# -------------------------------------------------------

matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0]
]
print("Matrix:")
for row in matrix:
    print(row)

# -------------------------------------------------------
# 2. FLATTEN A 2D MATRIX INTO A SINGLE LIST
# -------------------------------------------------------

flat = [num for row in matrix for num in row]
print("Flattened:", flat)

# Equivalent to:
# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)

# -------------------------------------------------------
# 3. TRANSPOSE A MATRIX (swap rows ↔ columns)
# -------------------------------------------------------

# Traditional way
rows = len(matrix)
cols = len(matrix[0])
tMatrix = []
for i in range(cols):
    temp_tMatrix = []
    for j in range(rows):
        temp_tMatrix.append(matrix[j][i])
    tMatrix.append(temp_tMatrix)
print(tMatrix)

# Comprehension version
transposed_comp = [[row[i] for row in matrix] for i in range(cols)]
print("Transposed (comprehension):", transposed_comp)

# -------------------------------------------------------
# 4. APPLY TRANSFORMATIONS DURING FLATTENING
# -------------------------------------------------------

# Example: square every element while flattening
squared_flat = [num ** 2 for row in matrix for num in row]
print("Squared & flattened:", squared_flat)

# Example: filter out odd numbers
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print("Even numbers only:", even_flat)

# -------------------------------------------------------
# GRID LABELS FOR 3x3 MATRIX
# -------------------------------------------------------

# Build coordinate grid
grid = [[(x, y) for x in range(3)] for y in range(3)]
print("Coordinate grid:")
for row in grid:
    print(row)

# Turn into labeled positions like ('A1', 'A2', ...)
rows = "ABC"
cols = range(1, 4)
labels = [[f"{r}{c}" for r in rows] for c in cols]
print("Labeled grid:")
for row in labels:
    print(row)