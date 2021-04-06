
import numpy as np
def missing(x):
    n = sorted([x[i+1]-x[i] for i in range(len(x)-1)])[0]
    c = np.arange(x[0],x[-1]+n,n)
    return [i for i in c if i not in x][0]

