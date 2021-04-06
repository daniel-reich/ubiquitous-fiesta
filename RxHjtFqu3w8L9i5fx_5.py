
def f(n):
    return 1 if n <1 else n*f(n-1)
def bell(n):
    return n or 1 if n <3 else sum(bell(k)*f(n-1)//(f(k)*f(n-1-k)) for k in range(n))

