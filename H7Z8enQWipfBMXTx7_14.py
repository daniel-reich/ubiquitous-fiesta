
def fib_str(n, f):
    if len(f) == n:
        return ', '.join(x for x in f)
    f.append(f[-1] + f[-2])
    return fib_str(n, f)

