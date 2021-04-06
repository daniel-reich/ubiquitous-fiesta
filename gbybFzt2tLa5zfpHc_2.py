
from itertools import*
def three_sum(l):
  c,l=combinations(l,3),[]
  for x in c:
    x=list(x)
    if sum(x)==0and x not in l:l.append(x)
  return l

