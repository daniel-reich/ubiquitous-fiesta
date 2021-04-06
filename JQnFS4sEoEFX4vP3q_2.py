
from itertools import combinations as C
def product_pair(lst, k):
  if k<=len(lst):
    A=[x for x in C(lst, k)]
    B=[]
    for x in A:
      p=1
      for y in x:
        p*=y
      B.append(p)
    return (min(B), max(B))
  else:
    return None

