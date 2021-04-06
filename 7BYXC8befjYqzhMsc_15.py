
import math
def classify_rug(alist):
    m = len(alist)
    n = len(alist[0])
    hcheck = 1
    if m>=2:
        for k in range(0, math.floor(m/2)+1):
            if alist[k]!=alist[m-1-k]:
                hcheck = 0
    vcheck = 1
    if n>=2:
        for k in range(0, math.floor(n/2)+1):
            ck = [alist[p][k] for p in range(0, m)]
            crk = [alist[p][n-1-k] for p in range(0, m)]
            if ck!=crk:
                vcheck = 0
    if (hcheck+vcheck==2):
        return "perfect"
    elif hcheck==1:
        return "horizontally symmetric"
    elif vcheck==1:
        return "vertically symmetric"
    else:
        return "imperfect"

