
def fair_swap(l1, l2):
    s, swap = set(), False
    if sum(l1) < sum(l2):
        l1, l2 = l2, l1
        swap = True
    one, two = sum(l1), sum(l2)
    if (one + two) % 2 == 1:
        return s
    dif = one - two
    for i in l1:
        look = i - (dif // 2)
        if look in l2:
            if swap:
                add = (look, i)
            else:
                add = (i, look)
            s.add(add)
    return s

