
from collections import*
def is_valid(t):
  v=sorted(Counter(t).values())
  if len(set(v))>2:return'NO'
  if len(set(v))<2:return'YES'
  return('NO','YES')[abs(v[0]-v[-1])==1and(1in[v.count(v[0]),v.count(v[-1])])]

