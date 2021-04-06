
def is_shifted(lst1, lst2):
    shift = lst2[0] - lst1[0]
    return [i+shift for i in lst1] == lst2
def is_multiplied(lst1, lst2):
    mult = lst2[0] / lst1[0]
    return [i*mult for i in lst1] == lst2

