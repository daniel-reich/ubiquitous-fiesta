
def fib_str(n, f):
    if n == 2:
        return ", ".join(f)
    else:
        add = f[-1] + f[-2]
        f.append(add)
        return fib_str(n - 1, f)

