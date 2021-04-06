
import numpy as np
def persistence(num):
    if len(str(num))==1:
        return 0
    count=1
    p = np.product([x for x in map(int,str(num))])
    while len(str(p))!=1:
        p = np.product([x for x in map(int,str(p))])
        count+=1
    return count

