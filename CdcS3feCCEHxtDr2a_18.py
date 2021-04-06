
from collections import Counter
from operator import itemgetter
def clear_ordering(lst):
    bb=[x for row in lst for x in row]
    cc=Counter(bb)
    tt=[k for k, v in cc.items() if v ==1]
    dic={x:row.index(x) for row in lst for x in row if x in tt}
    if min(list(dic.values())) != 0:
        return False
    sd=list(dic.keys())[list(dic.values()).index(0)]
    n=len(lst)
    for j in range(0,n):
        if sd == [row for row in lst if sd in row][0][0]:
            r = [row for row in lst if sd in row][0]
            sd = [row for row in lst if sd in row][0][1]
            lst.remove(r)
            if len(lst) == 0:
                return True
        else:
            return False

