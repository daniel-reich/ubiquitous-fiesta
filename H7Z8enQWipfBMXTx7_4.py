
def fib_str(n, f):
    if n-2==0:
        return ', '.join(f)
    else:
        f.append(f[len(f)-1]+f[len(f)-2])
    return fib_str(n-1, f)

