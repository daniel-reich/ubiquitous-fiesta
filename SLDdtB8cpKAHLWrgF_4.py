
from itertools import permutations as p
def greater_permutation(expr, nums):
  lst = [list(i) for i in p(nums,3)]
  high, res = -1, []
​
  for i in lst:
    a, b, c = i
    if eval(expr) > high:
      high, res = eval(expr), i
​
  for ch in 'abc':
    expr = expr.replace(ch,str(res.pop(0)))
​
  if high == int(high):
    high = int(high)
  else:
    high = round(high,2)
  
  return expr + ' = {}'.format(high)

