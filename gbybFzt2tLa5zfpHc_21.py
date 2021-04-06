
from itertools import combinations
def three_sum(lst):
  s=0
  ml=[]
  r=combinations(lst,3)
  for i in r:
      for d in i:
        s=s+d
      if s==0:
        ml.append(list(i))
      s=0
  w=[]
  b=[]
  for m in ml:
    if m in w:
      continue
    else: 
      b.append(m)
      w.append(m)
  return w

