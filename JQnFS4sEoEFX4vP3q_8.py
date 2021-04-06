
from itertools import combinations
from functools import  reduce
def product_pair(lst, k):
    ans = list(map(list,list(combinations(lst,k))))
    ans = sorted(list(map(lambda x:reduce(lambda z,y:z*y,x),ans))) if len(ans)!=0 else None
    return (ans[0],ans[-1]) if ans else None

