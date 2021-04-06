
def drange(*args):
    d = max([decs(a) for a in args])
    z = [int(a * 10**d) for a in args]
    lov = list(range(*z))
    return tuple(round(x/10**d, d) for x in lov)
 
def decs(x):
    s = str(x)
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1

