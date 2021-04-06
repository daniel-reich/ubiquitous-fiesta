
import numpy as np
​
def is_orthogonal(*argv):
    d=[]
    for m in range (len(argv)-1):
        for n in range(len(argv)-(m+1)):
            a=np.dot(argv[m],argv[n+m+1])
            d.append(a)
    return np.linalg.norm(d)==0

