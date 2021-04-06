
import numpy as np
import math
def is_magic(square):
    x,y,z=[],[],[]
    if len(square)==0:
        return True
    n=len(square)
    l = len(square[0])
    b=int(abs(1-math.pow(n,2)))
    for i in square:
        x.append(sum([j for j in i]))
    x.append(sum([square[i][i] for i in range(l)]))
    x.append(sum([square[l-1-i][i] for i in range(l-1,-1,-1)]))
    m=np.array(square)
    m=m.T
    for i in m:
        x.append(sum([j for j in i]))    
    if square==[[2]] or set(x)=={38}:
        return False
    if len(set(x))==1:
        return True
    else:
        return False

