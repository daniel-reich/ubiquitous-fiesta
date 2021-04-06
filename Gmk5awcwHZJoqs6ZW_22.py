
from collections import defaultdict
def largest_island(lst):
    d = defaultdict(list)
    for m in range(len(lst)):
        for n in range(len(lst[0])):
            if lst[m][n] == 1:
                for i in list(d):
                    if (abs(d[i][-1][0] -m)<=1 and abs(d[i][-1][1] - n)<=1):
                        d[i].append((m,n))
                    else:
                        d[(m,n)].append((m,n))
                if not d:
                    d[(m,n)].append((m,n))
    return(max(len(i) for i in list(d.values())))

