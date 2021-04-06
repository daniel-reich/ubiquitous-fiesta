
from math import factorial
​
def nespers(lst):
  n = factorial(len(lst))
  for e in lst:
    if type(e) == list:
      n *= nespers(e)
  return n

