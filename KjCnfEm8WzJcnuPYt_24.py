
from itertools import combinations as C, groupby as gb
def zero_indices(lst, k):
  A=[i for i, x in enumerate(lst) if not x]
  S=[]
  for x in C(A,k):
    lst2=lst.copy()
    for y in x:
      lst2[y]+=1
    B=[list(g) for t, g in gb(lst2) if t]
    S.append((list(x),len(max(B, key=len))))
  return sorted(S, key=lambda x: (-x[1], x))[0][0]

