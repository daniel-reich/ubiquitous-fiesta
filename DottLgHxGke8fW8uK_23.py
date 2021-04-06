
from functools import reduce
def nPr(n, r):
 return reduce(lambda x,y: x*y, range(n-r+1, n+1), 1)
 
def nCr(n, r):
 if r < n-r:
  return nPr(n, r) // reduce(lambda x,y: x*y, range(1, r+1), 1)
 return nPr(n, n-r) // reduce(lambda x,y: x*y, range(1, n-r+1), 1)

