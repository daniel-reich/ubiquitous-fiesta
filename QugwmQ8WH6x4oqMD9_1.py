
def count_identical_lists(lst1, lst2, lst3, lst4):
    a = [lst1, lst2, lst3, lst4]
    return len([i for i in a if a.count(i) > 1])

