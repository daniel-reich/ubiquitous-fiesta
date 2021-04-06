
from math import factorial
​
def grid_pos(lst):
  res = (factorial(sum(lst)) / factorial(max(lst)) )/ factorial(min(lst))
  return int(res)

