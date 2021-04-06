
from itertools import combinations 
def get_subsets(lst,n):
    out = []
    for i in range(1,len(lst)+1):
        r = list(combinations(lst,i))
        for m in r:
            if sum(m) ==n :
                out.append((len(list(m)), list(m)))
    a = [i[1] for i in sorted(out)]
    return a

