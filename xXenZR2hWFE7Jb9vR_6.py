
def is_isomorphic(s, t):
    lst1 = sorted(set(s), key=lambda c: s.index(c))
    lst2 = sorted(set(t), key=lambda c: t.index(c))
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        pos1 = [idx for idx, c in enumerate(s) if c == lst1[i]]
        pos2 = [idx for idx, c in enumerate(t) if c == lst2[i]]
        if pos1 != pos2:
            return False
    return True

