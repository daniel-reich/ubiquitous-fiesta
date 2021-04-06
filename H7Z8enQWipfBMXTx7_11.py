
def fib_str(n, f):
    return fib_str(n-1, f+[f[-1]+f[-2]]) if n>2 else ', '.join(f)

