
def drange(*args):
    if len(args) == 1:
        a, b, step = 0, args[0], 1
    elif len(args) == 2:
        a, b = args
        step = 1
    else:
        a, b, step = args
​
    res = [a]
    while a + step < b:
        a += step
        res.append(round(a, 3))
    return tuple(res)

