
from numpy import prod
def nPr(n, r):
  if r == 1:
    return n
​
  top = set(range(1,n+1))
  bot = set(range(1,(n-r)+1))
  return prod(list(top - bot))
​
def nCr(n, r):
  if r == 1:
    return n
  elif n == r:
    return 1
​
  s_n = set(range(1,n+1))
  s_r = set(range(1,r+1))
  s_nr = set(range(1,(n-r)+1))
  top = (s_n - s_nr) - s_r
  bot = s_r - (s_n - s_nr)
  return prod(list(top))/prod(list(bot))

