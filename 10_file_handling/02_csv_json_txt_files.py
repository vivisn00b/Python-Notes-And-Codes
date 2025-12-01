# --------------------------------------------------
# FILE HANDLING: TEXT, CSV, and JSON
# --------------------------------------------------

import csv
import json
import os

# 1 Working with TEXT files
print("TEXT FILES")

# Writing to a file
with open("notes.txt", "w") as file:
    file.write("Python File Handling Basics\n")
    file.write("Text, CSV, and JSON formats\n")

# Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)
print("-" * 50)


# 2 Working with CSV files (comma-separated values)
print("CSV FILES")

# Data we’ll save to a CSV file
employees = [
    {"name": "Amit", "dept": "HR", "salary": 50000},
    {"name": "Priya", "dept": "IT", "salary": 65000},
    {"name": "Rahul", "dept": "Finance", "salary": 60000}
]

# Writing CSV
with open("employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "dept", "salary"])
    writer.writeheader()
    writer.writerows(employees)

# Reading CSV
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} works in {row['dept']} and earns ₹{row['salary']}")
print("-" * 50)


# 3 Working with JSON files
print("JSON FILES")

# JSON is the universal data format — used in APIs and analytics pipelines
data = {
    "company": "DataWorks",
    "employees": employees,
    "location": "India"
}

# Write JSON
with open("company.json", "w") as file:
    json.dump(data, file, indent=4)

# Read JSON
with open("company.json", "r") as file:
    json_data = json.load(file)

print("Company name:", json_data["company"])
print("Employee count:", len(json_data["employees"]))
print("-" * 50)


# EXAMPLE 1:
data = [
    {"name": "Vivek", "city": "Kolkata, WB", "age": 21},
    {"name": "Harsha", "city": "Mysore, KA", "age": 25}
]
with open("people.tsv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "city", "age"],
        delimiter="\t",     # Gives tab separated values in file
        quoting=csv.QUOTE_MINIMAL      # Quoting controls when and how fields are wrapped in " "
    )
    # The quoting modes
    #
    # csv.QUOTE_MINIMAL: Quote only when needed (default).
    # So "Kolkata, WB" gets quoted, ordinary fields don’t.
    #
    # csv.QUOTE_ALL: Quote everything.
    #
    # csv.QUOTE_NONNUMERIC: Quote everything except numbers.
    # Safe for datasets mixing text + numbers.
    #
    # csv.QUOTE_NONE: Never quote anything
    # Risky but useful in strict pipelines.

    writer.writeheader()
    writer.writerows(data)


# EXAMPLE 2:
data = {
    "company": "XYZ InfoTech",
    "employees": [
        {"name": "Amit", "dept": "HR", "salary": 50000},
        {"name": "Priya", "dept": "IT", "salary": 65000},
        {"name": "Rahul", "dept": "Finance", "salary": 60000}
    ],
    "location" : "India"
}
with open("company.json", "w") as file:
    json.dump(data, file, indent=4)

with open("company.json", "r") as file:
    loaded = json.load(file)
print("Company:", loaded["company"])
print("Employees:", len(loaded["employees"]))
