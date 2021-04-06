
import numpy as np
def polygon(lst):
    v=len(lst)
    xc,yc=sum([lst[a][0] for a in range(v)])/v,sum([lst[a][1] for a in range(v)])/v
    lst=[[lst[a][0]-xc,lst[a][1]-yc] for a in range(v)]
    for a in range(v):
        lst[a].append(np.arctan2(lst[a][1],lst[a][0]))
    lst=sorted(lst,key=lambda h:h[2])
    lst.append(lst[0])    
    return abs(sum([lst[i][0]*lst[i+1][1]-lst[i][1]*lst[i+1][0] for i in range(v)])/2)

