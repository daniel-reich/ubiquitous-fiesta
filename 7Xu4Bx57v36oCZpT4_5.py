
import numpy as np
def where_is_waldo(lst):
    a,b = sorted(set([j for i in lst for j in i]))
    n,m=np.where(np.array(lst)==b)
    return [n[0]+1,m[0]+1]

