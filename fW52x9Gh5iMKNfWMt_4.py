
def recaman_index(n):
    r = [0]
    while r[-1] != n:
        s = r[-1] - len(r)
        if s > 0 and s not in r:
            r.append(s)
        else:
            r.append(r[-1] + len(r))
    return r.index(n)

