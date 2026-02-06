"""
===========================================
NumPy File I/O — Data Engineering Notes
===========================================

Use NumPy File I/O when:
- Data is purely numeric
- Schema is simple and fixed
- You want FAST intermediate storage
- You want to avoid CSV parsing overhead

Avoid NumPy File I/O when:
- Data has strings + numbers
- Complex schemas
- You need joins / column operations (use Pandas)
"""

import numpy as np

# -------------------------------------------------
# 1. np.loadtxt()
# -------------------------------------------------
"""
- Loads data from a text file into a NumPy array.

USES:
- Clean numeric data
- No missing values
- Small to medium files

IMPORTANT NOTES:
- Everything becomes float by default
- Breaks if file has missing values or mixed types
"""

# Example file format (data.txt):
# 10 20 30
# 40 50 60
# 70 80 90

data_loadtxt = np.loadtxt(
    "data.txt",        # file path
    delimiter=" ",     # separator (space, comma, tab)
    dtype=np.float64   # force dtype (optional)
)

print("loadtxt output:")
print(data_loadtxt)


# -------------------------------------------------
# 2. np.genfromtxt()
# -------------------------------------------------
"""
- Safer version of loadtxt
- Handles missing values and headers

USES:
- Real-world messy numeric files
- CSVs with missing values

IMPORTANT NOTES:
- Slower than loadtxt
- Missing values become np.nan
"""

# Example file format (data.csv):
# id,score
# 1,90
# 2,
# 3,85

data_genfromtxt = np.genfromtxt(
    "data.csv",
    delimiter=",",
    skip_header=1,     # skip column names
    dtype=float,       # numeric output
    filling_values=0  # optional: replace missing values
)

print("\ngenfromtxt output:")
print(data_genfromtxt)


# -------------------------------------------------
# 3. np.save() and np.load()
# -------------------------------------------------
"""
- Saves NumPy arrays in binary (.npy) format
- Preserves shape and dtype

USES:
- Intermediate ETL storage
- Caching processed data
- Very fast load/save

IMPORTANT NOTES:
- Not human readable
- Much faster than CSV
"""

arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

# Save array to disk
np.save("my_array.npy", arr)

# Load array from disk
loaded_arr = np.load("my_array.npy")

print("\nSaved and loaded array:")
print(loaded_arr)
print("dtype:", loaded_arr.dtype)
print("shape:", loaded_arr.shape)


# -------------------------------------------------
# 4. np.savez() — save multiple arrays
# -------------------------------------------------
"""
- Saves multiple NumPy arrays into one compressed file (.npz)

USES:
- Store features + labels
- Bundle related arrays together
"""

X = np.array([[10, 20], [30, 40]])
y = np.array([0, 1])

np.savez(
    "dataset_bundle.npz", features=X, labels=y)

# Load bundled arrays
bundle = np.load("dataset_bundle.npz")
features = bundle["features"]
labels = bundle["labels"]

print("\nLoaded from .npz:")
print("features:", features)
print("labels:", labels)


# -------------------------------------------------
# 5. Memory Mapping (VERY IMPORTANT FOR DEs)
# -------------------------------------------------
"""
- Loads array without reading entire file into RAM

USES:
- Huge arrays
- Low-memory environments
- Batch processing

IMPORTANT NOTES:
- Data is read from disk on demand
- Read-only or read-write modes
"""

big_array = np.load("my_array.npy", mmap_mode="r")

print("\nMemory-mapped array:")
print(big_array)


# -------------------------------------------------
# 6. Real ETL-style NumPy workflow
# -------------------------------------------------
"""
ETL FLOW:
Extract -> Transform -> Load (cache)

WHY THIS IS IMPORTANT:
- Avoid reprocessing
- Avoid CSV parsing
- Faster pipelines
"""

# Extract
raw_data = np.loadtxt("data.txt")

# Transform (masking example)
clean_data = raw_data[raw_data[:, 1] > 30]

# Load (cache transformed data)
np.save("clean_data.npy", clean_data)

# Reload later (fast)
cached_data = np.load("clean_data.npy")

print("\nETL cached data:")
print(cached_data)


# -------------------------------------------------
# INTERVIEW SUMMARY (MEMORIZE)
# -------------------------------------------------
"""
- loadtxt(): fast, clean numeric files
- genfromtxt(): handles missing values, slower
- save/load(): fastest way to store NumPy arrays
- savez(): bundle multiple arrays
- mmap_mode: handle massive datasets efficiently

Golden Rule:
Binary formats (.npy/.npz) >> CSV for performance
"""