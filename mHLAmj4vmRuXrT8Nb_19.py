
def consecutive_combo(lst1, lst2):
    combn = lst1 + lst2
    combn.sort()
    return combn == [i for i in range(min(combn), max(combn)+1)]

