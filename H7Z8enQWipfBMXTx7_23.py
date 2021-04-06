
def fib_str(n, f):
    if n == 2:
        return f[0] + ", " + f[1]
    else:
        return fib_str(n - 1, f) + ", " + fib_str(n - 1, f).split(", ")[-1] + fib_str(n - 1, f).split(", ")[-2]

