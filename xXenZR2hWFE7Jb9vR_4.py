
from collections import*
def is_isomorphic(s,t):
  d=defaultdict(set)
  for x,y in zip(s,t):d[x].add(y)
  return all(len(d[x])==1for x in d)and len(d)==len(set(d[x].pop()for x in d))

