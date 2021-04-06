
def fibonacci(n):
    if n < 3: return 1
    fib, i, f = [1, 1, 2], 1, 2 
    while f < n:
        i = (i + 1) % 3
        fib[i] = (fib[1] + fib[2]) if i == 0 else (fib[0] + fib[2]) if i == 1 else (fib[0] + fib[1])
        f += 1
    return fib[i]

