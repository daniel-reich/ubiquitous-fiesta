
from itertools import combinations_with_replacement as H
def football(score):
  s=[2,3,6,7,8]
  if score:
    A=[]
    for i in range(0,score//2+1):
      A+=list(H(s,i))
    B=[x for x in A if sum(x)==score]
    return len(B)
  return 1

