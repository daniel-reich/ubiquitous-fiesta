
def consecutive_combo(l1, l2):
    l = sorted(l1 + l2)
    return l == list(range(l[0],l[-1]+1))

