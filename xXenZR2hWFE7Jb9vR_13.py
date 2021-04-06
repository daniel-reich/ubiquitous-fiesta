
def is_isomorphic(s, t):
    d1, d2 = {}, {}
    for a, b in zip(s, t):
        if a in d1 and d1[a] != b:
            return False
        d1[a] = b
        if b in d2 and d2[b] != a:
            return False
        d2[b] = a
    return True

