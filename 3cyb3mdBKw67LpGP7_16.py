
from itertools import groupby
def numbers_need_friends_too(n):
    k = ''
    for lst in [list(g) for k, g in groupby(str(n))]:
        if len(lst)==1:
            k+=lst[0]*3
        else:
            k+=''.join(lst)
    return int(k)

