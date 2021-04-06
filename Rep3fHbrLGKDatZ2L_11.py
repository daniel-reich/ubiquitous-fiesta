
from itertools import cycle
def complete_pattern(s):
  S=set(s.replace('_', ''))
  res=''
  for x in S:
    p=s.replace('_', x)
    if any(all(x==y for x, y in zip(p,cycle(p[:i]))) for i in range(1, len(p)//2+1)):
      res+=x
  return res

