
from itertools import groupby
def group_seats(lst, n):
    cnt=0
    for r in enumerate(lst):
        hy=[(len(list(r1[1]))) for r1 in groupby(r[1]) if r1[0]==0]
        for r in hy:
            if n<r:
                cnt+=2
            if n==r:
                cnt+=1
            else:
                continue
    return cnt

