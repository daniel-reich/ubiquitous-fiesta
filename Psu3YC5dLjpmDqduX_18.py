
import math
def angle(P1,P2):
    k=(P2[1]-P1[1])/((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)**.5
    x1, x2=P1[0], P2[0]
    if k>=0:
        if x2>=x1:
            return 2*math.pi-math.asin(k)
        else:
            return math.pi+math.asin(k)
    else:
        if x2>=x1:
            return math.asin(-k)
        else:
            return math.pi-math.asin(-k)
def polygon(lst):
  rpt=[sum(x[0] for x in lst)/len(lst), sum(x[1] for x in lst)/len(lst)]
  lst=sorted(lst, key=lambda x: -angle(x, rpt))
  p=0
  n=0
  for i in range(len(lst)):
    sidx=(i+1)%len(lst)
    pd=lst[i][0]*lst[sidx][1]
    p+=pd
  for i in range(len(lst)):
    sidx=(i+1)%len(lst)
    pd=lst[sidx][0]*lst[i][1]
    n+=pd
  return (p-n)*.5

