
from functools import reduce
def num_then_char(lst):
    flat = reduce(list.__add__, lst)
    flat.sort(key = lambda x: (type(x) is str, x))
    j = 0
    for i, v in enumerate(lst):
        lst[i] = flat[j:j+len(v)]
        j += len(v)
    return lst

