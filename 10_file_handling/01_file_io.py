# --------------------------------------------------
# Python File I/O — Reading, Writing, and Processing Data
# --------------------------------------------------

import os

# 1 Writing Text Files
print("Writing Text Files:")

data = """Name, Age, Department
Alice, 25, Data
Bob, 30, IT
Charlie, 28, HR
"""

# Write to file
with open("employees.txt", "w") as file:
    file.write(data)
print("Data written to employees.txt")
print("-" * 50)

# 2 Reading Files — Full, Line by Line
print("Reading Text Files:")

# Instead of manually opening and closing the file, you can use the with statement, which automatically handles closing.
# This reduces the risk of file corruption and resource leakage.
with open("employees.txt", "r") as file:
    content = file.read()  # read entire file
print("Full file content:\n", content)

with open("employees.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())

f = open('employees.txt', 'r')
print(f)
print(f.read())
f.close()
print("-" * 50)

# 3 Appending to Files
print("Appending Data:")

with open("employees.txt", "a") as file:
    file.write("David,35,Finance\n")
print("New record appended!")
print("-" * 50)

# 4 Reading CSV-Like Data (Manually)
print("Processing Data for Analytics:")

employees = []
with open("employees.txt", "r") as file:
    next(file)  # skips the header line ("Name,Age,Department")
    for line in file:
        name, age, dept = line.strip().split(",")
        employees.append({"name": name, "age": int(age), "department": dept})

print("Processed employee records:")
for e in employees:
    print(e)
print("-" * 50)

# 5 Calculating Insights
print("Simple Data Analytics Example:")

# Average age
ages = [e["age"] for e in employees]
avg_age = sum(ages) / len(ages)
print(f"Average age of employees: {avg_age:.2f}")

# Department-wise grouping
departments = {}
for e in employees:
    dept = e["department"]
    departments[dept] = departments.get(dept, 0) + 1     # .get(dept, 0) ensures we start counting from zero.
    # above line is similar to:
    #if dept in departments:
    #    departments[dept] += 1
    #else:
    #    departments[dept] = 1

print("Employees per department:")
for dept, count in departments.items():
    print(f"  {dept}: {count}")
print("-" * 50)


# 6 Deleting Files (Cleanup)
print("Deleting Files Safely:")

if os.path.exists("employees.txt"):
    os.remove("employees.txt")
    print("File deleted successfully.")
else:
    print("File not found.")
print("-" * 50)