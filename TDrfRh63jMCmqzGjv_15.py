
def is_anti_list(lst1, lst2):
    a = set(lst1) == set(lst2)
    b = all([x != y for x, y in zip(lst1, lst2)])
    return a and b

