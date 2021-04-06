
def fibonacci_sequence():
    fib, n = [0,1], 1
    while n<255:
        fib.append(n)
        n = fib[-1]+fib[-2]
    return fib

