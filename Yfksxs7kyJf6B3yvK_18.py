
def min_miss_pos(lst):
    lst2 = sorted([c for c in lst if c >= 0])
    lst3 = [i for i in range(min(lst2), max(lst2)+2) if i not in lst2]
    return min(lst3)

