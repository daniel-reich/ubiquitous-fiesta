
def zip_discard_compr(*iterables, sentinel=object()):
    from itertools import zip_longest
    return [[entry for entry in iterable if entry is not sentinel]
            for iterable in zip_longest(*iterables, fillvalue=sentinel)]
​
​
def bridge_shuffle(lst1, lst2):
    res = [list(x) for x in zip_discard_compr(lst1, lst2)]
    return [x for y in res for x in y]

