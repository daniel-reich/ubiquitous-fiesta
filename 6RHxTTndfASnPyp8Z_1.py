
from itertools import groupby
def compress(chars):
    res = []
    for k, g in groupby(chars):
        res.append(k)
        len_g = len(list(g))
        if len_g > 1:
            for x in str(len_g):
                res.append(x)
    return "".join(res)

