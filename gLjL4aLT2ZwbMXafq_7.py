
def fair_swap(l1, l2):
    l1.sort(); l2.sort()
    a, b = sum(l1), sum(l2); value = abs(a-b)
    if value % 2 != 0:
        return set()
    value, sol, pa, pb = value//2, set(), 0, 0
    inv = False
    if a > b:
        l1, l2 = l2, l1
        inv = True
    la, lb = len(l1), len(l2)
    vb, va = l2[pb], l1[pa]
    for _ in range(la+lb):
        dif = vb - va
        if dif > value:
            pa += 1
            if pa >= la:
                break
            va = l1[pa]
        elif dif < value:
            pb += 1
            if pb >= lb:
                break
            vb = l2[pb]
        else:
            if inv:
                sol.add((vb, va))
            else:
                sol.add((va, vb))
            pa += 1
            pb += 1
            if pb >= lb or pa >= la:
                break
            va, vb = l1[pa], l2[pb]
    return sol

