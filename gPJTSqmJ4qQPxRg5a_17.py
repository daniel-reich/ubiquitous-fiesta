
def func(n):
    d = len(str(n))
    return -sum(d - int(i) for i in str(n))

