
from itertools import combinations
from collections import Counter
def ulam(n):
  res = [1,2]
  m = max(res)
  p = 2
  combis = [3]
  while p < n:
    m = min([k for k,v in Counter([combi for combi in combis]).items() if v == 1])
    combis = [combi for combi in combis if combi > m]
    combis.extend([q+m for q in res])
    res.append(m)
    p += 1
  return res[-1]

