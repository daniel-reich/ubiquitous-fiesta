
from functools import *
def num_ways(n,s):
  @lru_cache()
  def helper(n, m):
    if n <= 1:
      return n
    res,i = 0,1
    while i <= m and i <= n:
      res += helper(n-i,m)
      i += 1
    return res
  return helper(n+1,max(s))

