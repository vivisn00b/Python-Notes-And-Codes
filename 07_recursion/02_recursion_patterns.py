# Types of Recursion in Python:
# Tail Recursion: The recursive call is the last thing the function does, so nothing happens after it returns. Some languages can optimize this to work like a loop, saving memory.
# Non-Tail Recursion: The function does more work after the recursive call returns, so it can’t be optimized into a loop.
def nontail_fact(n):
    # Base case
    if n == 1:
        return 1
    # Non-tail recursive call because the multiplication happens after the call
    else:
        return n * nontail_fact(n-1)
# In normal recursion, every call waits for the next one to return a value.
# Each call is paused until the one beneath it finishes, so the multiplications happen after the recursive calls return.

def tail_fact(n, acc=1):
    # Base case
    if n == 0:
        return acc
    # Tail recursive call with an accumulator
    else:
        return tail_fact(n-1, acc * n)  # In tail recursion, we do the work before making the recursive call — we multiply acc * n and pass that forward as an argument to the next call.
# Each call passes its partial result (acc * n) forward to the next call.
# This avoids doing extra multiplications while unwinding the call stack.

# Example usage
print(tail_fact(5))
print(nontail_fact(5))