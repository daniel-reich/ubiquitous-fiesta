
def fib_str(n, f):        
    if n == 2:
        return', '.join(f)
    return fib_str(n-1, f + [f[-1] + f[-2]])

