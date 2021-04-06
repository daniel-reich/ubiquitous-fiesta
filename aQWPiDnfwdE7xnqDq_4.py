
def drange(*args):
    r = []
    g = iter(args)
    a = next(g)
    b = next(g, - 1)
    c = next(g, 1)
    if b == - 1:
        a, b = 0, a
    decimals = max(deci(a), deci(b), deci(c))
    while a < b:
        r.append(round(a, decimals))
        a += c
    return tuple(r)
    
def deci(x):    
    if type(x) == float:
        return len(str(x).split(".")[1])
    return 0

