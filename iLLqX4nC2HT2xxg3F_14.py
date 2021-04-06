
def deepest(l):
    d = []
    for i in l:
        if isinstance(i, list):
            d.append(deepest(i))
    if len(d) > 0:
        return 1 + max(d)
    return 1

