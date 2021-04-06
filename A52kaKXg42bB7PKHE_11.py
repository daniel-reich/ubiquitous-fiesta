
def num_then_char(lst):
    v = []
    w = []
    g = []
    s = []
    for i in lst:
        for y in i:
            v.append(y)
    for i in v:
        if i is str(i):
            w.append(i)
        else:
            g.append(i)
    g.sort()
    w.sort()
    r = g + w
    row = len(lst)
    cols = list(map(len, lst))
    p = 0
    k = cols[0]
    for i in range(1, row):
        s.append(r[p:k])
        p = k
        k += cols[i]
​
    s.append(r[p:k])
    return s

