
from functools import reduce
from operator import mul
​
def nPr(n, r):
  return reduce(mul, range(n-r+1, n+1), 1)
​
def nCr(n, r):
  a = max(r, n-r)
  b = n-a
  return reduce(mul, range(a+1, n+1), 1) // reduce(mul, range(1, b+1), 1)

