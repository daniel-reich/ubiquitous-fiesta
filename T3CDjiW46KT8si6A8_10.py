
from heapq import nlargest
​
def product(lst):
  *a, b = sorted(set(lst), reverse=True)[:2]
  return a[0] * b if a else b * b

