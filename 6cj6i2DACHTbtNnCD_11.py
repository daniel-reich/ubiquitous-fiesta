
import itertools
def two_product(lst, n):
    lst.sort()
    a = list(filter(lambda x:list(x)[0]*list(x)[1]==n, list(itertools.combinations(lst,2))))
    return sum(list(map(lambda x:list(x),a)),[]) if len(a)!=0 else None

