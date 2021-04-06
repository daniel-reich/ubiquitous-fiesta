
def consecutive_combo(lst1, lst2):
    clst = lst1 + lst2
    return list(range(min(clst), min(clst)+len(clst))) == sorted(clst)

