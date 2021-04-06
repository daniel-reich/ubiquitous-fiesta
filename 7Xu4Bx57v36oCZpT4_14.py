
def where_is_waldo(lst):
    x = 1 + [len(set(x)) for x in lst].index(2)
    y = 1 + [len(set(x)) for x in zip(*lst)].index(2)
    return [x, y]

