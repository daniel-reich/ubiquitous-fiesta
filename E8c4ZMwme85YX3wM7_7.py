
def recaman(n):
    p = [0]
    for x in range(1, n):
        a = p[-1] - x
        if a > 0 and a not in p:
            p.append(a)
        else:  
            a = p[-1] + x
            p.append(a)
    if n == 0:
        p = []
    d = [p[x] for x in range(len(p)) if p[: x + 1].count(p[x]) == 2]
    return "---> Recaman's sequence: {}\n---> Duplicates for n = {}: {}".format(p, n, d)

