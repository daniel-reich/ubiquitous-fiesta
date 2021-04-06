
def intersection_union(lst1, lst2):
    intersection = list(set([x for x in lst1 if x in lst2]))
    intersection.sort()
    union = list(set(lst1 + lst2))
    union.sort()
    return [intersection, union]

