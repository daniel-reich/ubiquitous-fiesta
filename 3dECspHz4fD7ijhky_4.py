
from itertools import groupby
from operator import itemgetter
def numbers_range(ranges):
    nums = sorted(set(ranges))
    gaps = [[s, e] for s, e in zip(ranges, ranges[1:]) if s+1 < e]
    edges = iter(ranges[:1] + sum(gaps, []) + ranges[-1:])
    a=list(zip(edges, edges))
    res=''
    for i in a:
        if i[0]-i[1]==0:
            res+=str(i[0])+', '
        elif abs(i[0]-i[1])==1:
            res+=str(i[0])+', '+str(i[1])+', '
        else:
            res+=str(i[0])+'-'+str(i[1])+', '
    return res[0:-2].strip()

