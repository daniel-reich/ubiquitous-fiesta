
def number_pairs(t):
    v, p, p1, r, t = [i +" " for i in t.split()[1:]], set(), -1, 0, t+" "
    for i in v:
        p1 = t.find(i, p1 + 1)
        p2 = t.find(i, p1 + 1)
        if p2 > p1 and {p1, p2}.intersection(p)==set():
            p.update([p1, p2])
            r += 1
    return r

