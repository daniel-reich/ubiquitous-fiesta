
from functools import reduce
​
def helper(x, y):
  return helper(y, x % y) if y else x
​
def gcd(lst):
  return reduce(helper, lst)

