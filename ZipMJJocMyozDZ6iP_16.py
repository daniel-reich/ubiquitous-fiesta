
from math import ceil
​
def group(lst, size):
  q  = ceil(len(lst)/size)
  out = [[] for l in range(q)]
  while lst:
    for x in range(q):
      if lst: out[x].append(lst.pop(0))
      else: break
  return out

