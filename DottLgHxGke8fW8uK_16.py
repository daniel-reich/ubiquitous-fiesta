
from numpy import prod
​
def nPr(n, r):
  return prod(range(n-r+1, n+1))
​
def nCr(n, r):
  return prod(range(max(r, n-r)+1, n+1)) / prod(range(1, min(r, n-r)+1))

