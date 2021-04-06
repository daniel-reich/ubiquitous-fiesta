
def simon_says(lst1, lst2):
    return all(el1 == el2 for el1, el2 in zip(lst1, lst2[1:]))

