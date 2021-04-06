
from functools import reduce
def primorial(n):
  p = []; i=2
  while len(p) < n:
    if all(i%j for j in range(2,i)):
      p.append(i)
    i += 1
  return reduce(lambda x, y: x*y, p)

