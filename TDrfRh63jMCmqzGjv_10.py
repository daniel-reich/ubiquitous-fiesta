
def is_anti_list(lst1, lst2):
    return (set(lst1) == set(lst2) and
            len(set(lst1)) == 2 and
            not sum(a==b for a, b in zip(lst1, lst2)))

