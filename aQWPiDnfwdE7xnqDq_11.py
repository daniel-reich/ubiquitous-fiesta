
def drange(*args):
    if len(args) == 1:
        a, b, c = 0, args[0], 1
    elif len(args) == 2:
        a, b, c = args[0], args[1], 1
    else:
        a, b, c = args
    if c == 1:
        return tuple(list(range(a, b)))
    digits = max(len(str(c).split('.')[1]), len(str(float(a)).split('.')[1]))
    ans = [a]
    k = 0
    while True:
        k += 1
        d = round(a + k * c, digits)
        if d >= b:
            break
        ans.append(d)
    return tuple(ans)

