
def intersection_union(lst1, lst2):
    int_sec = set(lst1).intersection(set(lst2))
    union_list = set(lst1).union(set(lst2))
    return [sorted(int_sec), sorted(union_list)]

