
def is_parallelogram(lst):
    mids = []
    a, b, c, d = lst
    pts = [(a,b), (a,c), (a,d), (c,d), (b,d), (b,c)]
    for p in pts:
        m = get_midpt(p)
        if m in mids:
            return True
        mids.append(m)
    return False
​
def get_midpt(p):
    p1, p2 = p
    x1, y1 = p1
    x2, y2 = p2
    return (x1+x2, y1+y2)

