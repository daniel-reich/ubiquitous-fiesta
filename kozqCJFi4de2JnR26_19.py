
def fib_str(n, txt):
    res = txt
    for u in range(2,n):
        res.append(res[u-1]+res[u-2])
    return ', '.join(res)

