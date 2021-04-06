
def intersection_union(lst1, lst2):
    intersection = sorted(list(set([i for i in lst1 if i in lst2])))
    union = sorted(list(set(lst1 + lst2)))
    return [intersection, union]

