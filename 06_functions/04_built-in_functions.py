# LAMBDA: Lambda Functions are anonymous functions means that the function is without a name
# lambda arguments: expression
#
# | Code               | What it does                          |
# | ------------------ | ------------------------------------- |
# | `lambda x: x*10`   | waits for user input                  |
# | `lambda: x*10`     | captures variable (late binding risk) |
# | `lambda x=x: x*10` | freezes value (early binding)         |
#
# Examples:
x = 5
f = lambda: x * 10
print(f())

# 1. Using with Condition Checking
n = lambda x: "Positive" if x>0 else "Negative" if x<0 else "Zero"
print(n(5))
print(n(-3))
print(n(0))

# 2. Using with List Comprehension
li = [lambda arg=x: arg*10 for x in range(1, 5)]     # list of functions
# Internally it is like:
#li = [
#     lambda arg=1: arg * 10,
#     lambda arg=2: arg * 10,
#     lambda arg=3: arg * 10,
#     lambda arg=4: arg * 10
# ]
# Simpler version:
#li = []
#
#for x in range(1, 5):
#    def f(arg=x):
#        return arg * 10
#    li.append(f)
#print(li[0], li[1], li[2], li[3])
print(li[0](), li[1](), li[2](), li[3]())
for i in li:
    print(i())

# 3. Using for Returning Multiple Results
calc = lambda x, y: (x+y, x*y)
res = calc(2, 3)
print(res)


# MAP: applies a given function to each element of an iterable (list, tuple, set, etc.) and returns a map object (iterator)
# higher-order function used for uniform element-wise transformations, enabling concise and efficient code.
#
# Examples:
s = ['1', '2', '3', '4']
res = map(int, s)
#print(res)
print(list(res))

# Without lambda:
def square(num):
    return num ** 2
nums = [1, 2, 3, 4, 5]
res = map(square, nums)
print(list(res))
# Using lambda:
nums = [1, 2, 3, 4]
result = map(lambda x: x * x, nums)
print(list(result))

# With multiple iterables:
a = [1, 2, 3]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)
print(list(result))