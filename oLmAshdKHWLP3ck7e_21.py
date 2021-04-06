
from itertools import combinations
def min_difference_pair(nums):
  a=nums
  b=list(combinations(a,2))
  c=[]
  for i in range(len(b)):
      x=abs(b[i][0]-b[i][1])
      c.append([b[i],x])
  y=sorted(c,key=lambda x:x[1])
  z=(y[0][1])
  w=[]
  for i in range(len(y)):
      if y[i][1]==z:
          w.append(y[i][0])
  m=[]
  for i in range(len(w)):
      m.append([w[i],sum(w[i])])
  n=sorted(m,key=lambda x:x[1])
  p=list((n[0][0]))
  p.sort()
  return(p)

