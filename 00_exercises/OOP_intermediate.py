# 1. Create a class BankAccount
# Attributes: account_number, balance
# Methods: deposit(), withdraw()
# Prevent withdrawing more than balance.
# 2. Demonstrate encapsulation by making balance private.
# 3. Create a base class Employee and child class Developer
# Override a method in child class.

# 1,2
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount
        return self.__balance

    @property
    def balance(self):
        return self.__balance

print(BankAccount(100, 100).deposit(10000))
# print(BankAccount(100, 100).withdraw(10000))
viv_savings_ac = BankAccount(123456789, 35000)
print(viv_savings_ac.balance)
viv_savings_ac.deposit(10000)
print(viv_savings_ac.withdraw(5555))

# 2,3
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_role(self):
        return "Employee"

    def calculate_bonus(self):
        return self.salary * 0.10

class Developer(Employee):
    def get_role(self):
        return "Developer"

    class Developer(Employee):
        def calculate_bonus(self):
            base_bonus = super().calculate_bonus()
            return base_bonus + (self.salary * 0.05)

emp = Employee("John", "", 50000)
dev = Developer("Alice", "", 80000)

print(emp.get_role())   # Employee
print(dev.get_role())   # Developer
print(f"{dev.first_name}'s bonus: {dev.calculate_bonus()}")