
import itertools
def deepest(lst):
    depth=0
    while lst:
        depth+=1
        merged = list(itertools.chain(*[elem for elem in lst if   isinstance(elem,list)]))
        lst=merged[:]
    return depth

