
from itertools import groupby as gb
def rank(lst):
  lst2=sorted(lst)
  A=[(x,list(g)) for x, g in gb(lst2)]
  B=[(x[0],sum(lst2.index(x[0])+i for i in range(len(x[1])))/len(x[1])) for x in A]
  D=dict(B)
  res=[D[x] for x in lst]
  return res

