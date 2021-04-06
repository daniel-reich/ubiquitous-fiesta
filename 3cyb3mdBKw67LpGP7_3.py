
from itertools import groupby
def numbers_need_friends_too(n):
  s=str(n)
  A=[list(g) for x, g in groupby(s)]
  B=[]
  for x in A:
    if len(x)==1:
      B.append(''.join(x*3))
    else:
      B.append(''.join(x))
  return int(''.join(B))

