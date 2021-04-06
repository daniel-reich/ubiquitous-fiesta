
from functools import reduce
​
def max_product(n):
  m = 0
  result = []
  while n > 0:
    if '0' in str(n):
      n -= 1
      continue
    newn = [int(x) for x in str(n)]
    total = reduce(lambda x,y: x*y,newn)
    if m == 0:
      m = total
      continue
​
    if total == m: result.append(n)
    if total > m:
      result = [n]
      m = total
    n -= 1
  return sorted(result)

