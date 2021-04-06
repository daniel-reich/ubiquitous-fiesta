
from itertools import combinations
def three_sum(lst):
    x,a=[],[]
    if len(lst)<3:
        return []
    else:
        comb =combinations(lst, 3)
        for i in comb:
            if sum(list(i))==0:
                x.append(list(i)) 
        dups=set()
        for i,route in enumerate(x):
            if tuple(route) in dups:
                a.append(i)
            else:
                dups.add(tuple(route))
        if len(a)==2:
            return x[:2]
        if len(a)==1:
            x.pop(a[0])
            return x
        if len(a)==3:
            x.pop(a[2])
            x.pop(a[1])
            x.pop(a[0])
            return x
        else:
            return x

