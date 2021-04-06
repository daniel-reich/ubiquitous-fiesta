
def to_list(dct):
    from collections import OrderedDict
    x = OrderedDict(sorted(dct.items()))
    return list(map(list,x.items()))

