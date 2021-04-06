
def intersection_union(lst1, lst2):
    set1, set2 = set(lst1), set(lst2)
    union = sorted(list(set1.union(set2)))
    intersection = sorted(list(set1.intersection(set2)))
    return [intersection, union]

