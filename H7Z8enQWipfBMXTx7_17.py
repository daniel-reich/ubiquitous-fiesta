
def fib_str(n, f):
    if n > 2:
        return f[0] + ', ' + fib_str(n-1, [f[1], f[1]+f[0]])
    return f[0] + ', ' + f[1]

