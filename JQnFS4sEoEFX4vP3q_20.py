
from itertools import combinations
​
def product_pair(lst, k):
  if k > len(lst):
    return
  combos = [prod(i) for i in combinations(lst, k)]
  return min(combos), max(combos)
  
def prod(lst):
  result = 1
  for i in lst:
    result *= i
  return result

