
def fair_swap(l1, l2):
    s = (sum(l1) - sum(l2)) // 2
    l1 = set(l1)
    res = set()
    for x in l2:
        if s + x in l1:
            res.add((s + x, x))
    return res

