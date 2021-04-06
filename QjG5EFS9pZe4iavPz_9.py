
def fib(n):
    f = [0, 1]
    while n >= len(f):
        f.append(f[-1] + f[-2])
    return f[n]

