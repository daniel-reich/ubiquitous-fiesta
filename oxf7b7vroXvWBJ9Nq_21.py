
def discount(n, txt):
    lop, loa = [], []
    lod = txt.split(', ')
    for x in lod:
        if not x:
            break
        if x[-1] == '%':
            lop.append(float(x[:-1]))
        else:
            loa.append(float(x))
    lop = sorted(lop, reverse=True)
    for x in lop:
        n = n * (100-x) * .01
    for x in loa:
        n = n - x
    return round(n, 2)

