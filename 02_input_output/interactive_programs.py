# -------------------------------------------------------
# 1. SIMPLE INPUT AND GREETING
# -------------------------------------------------------

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nHello {name}! You’re {age} years old.")
print(f"In 10 years, you’ll be {age + 10}.")

# -------------------------------------------------------
# 2. BASIC CALCULATOR
# -------------------------------------------------------

print("\nSimple Calculator")
print("="*25)
while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number:"))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        if choice == '1':
            print(num1, "+", num2, "=", num1+num2)
        if choice == '2':
            print(num1, "-", num2, "=", num1-num2)
        if choice == '3':
            print(num1, "*", num2, "=", num1*num2)
        if choice == '4':
            print(num1, "/", num2, "=", num1/num2)
        next_calc = input("Do you want to perform another calculation? (y/n): ")
        if next_calc.lower() != "y":
            break
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4)")

# -------------------------------------------------------
# 3. INTERACTIVE SALES REPORT
# -------------------------------------------------------

print("\nSales Data Entry")
print("=" * 25)

items = []
while True:
    name = input("Item name (or 'done' to finish): ").strip()
    if name.lower() == "done":
        break
    qty = int(input("Quantity sold: "))
    price = float(input("Unit price: "))
    items.append((name, qty, price))
    print(f"Added {name} x{qty} @ {price:.2f}\n")

# Compute totals
total_qty = sum(qty for _, qty, _ in items)
total_revenue = sum(qty * price for _, qty, price in items)

print("\n" + "=" * 40)
print(f"{'SALES SUMMARY':^40}")
print("=" * 40)
print(f"{'Item':<15}{'Qty':>10}{'Price':>10}")
print("-" * 35)
for name, qty, price in items:
    print(f"{name:<15}{qty:>10}{price:>10.2f}")
print("-" * 35)
print(f"{'TOTAL':<15}{total_qty:>10}{total_revenue:>10.2f}")
print("=" * 40)