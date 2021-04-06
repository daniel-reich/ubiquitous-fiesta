
def grouping(w):
    z = sorted([f(x) for x in w])
    d = {}
    for c, l, wd in z:
        if c not in d:
            d[c] = []
        d[c].append(wd)
    return d
    
def f(x):
    cnt = 0
    for ch in x:
        if ch.isupper():
            cnt += 1
    return (cnt, x.lower(), x)

