
def fib_str(n, txt):
    res = []
    a, b = txt[0], txt[1]
    while n > 2:
        a, b, n = b, b+a, n-1
        res.append(b)
    res.insert(0, txt[0])
    res.insert(1,txt[1])
    return ', '.join(res)

