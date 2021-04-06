
from itertools import permutations
from itertools import chain
from collections import Counter
def combo(lst, n):
  a=len(lst)
  newLst=[]
  outLst=[]
  if(n>a):
    return newLst
  else:
    subLst=[]
    if(n==0):
      newLst.append(subLst)
      return newLst
    else:
      perm = permutations(lst, n)
      z=sorted(set(perm))
      print("sorted unique permutations is: "+str(z))
      y=len(z)
      for i in range(0,y):
        x=z[i]
        w=sorted(x)
        newLst.append(w)
  outLst=Counter([tuple(q) for q in newLst])
  g=list(sorted(outLst.keys()))
  sLst=[]
  xLst=[]
  h=len(g)
  print(h)
  for k in range(0,h):
      m=g[k]
      p=len(m)
      print(p)
      for f in range(0,p):
          sLst.append(m[f])
      xLst.append(sLst)
      sLst=[]
  return xLst

