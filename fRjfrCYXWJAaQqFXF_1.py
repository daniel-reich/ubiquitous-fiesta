
from numpy import prod
​
def primorial(n):
  lst = [2]
  x = 3
  while len(lst) < n:
    for i in lst:
      if not x % i:
        x+=2
        continue
    lst.append(x)
    x += 2
  return prod(lst)

