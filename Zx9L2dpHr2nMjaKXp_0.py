
def int_to_vlq(n):
  if n == 0: return [0]
  arr = []
  while n:
    n, r = divmod(n, 128)
    arr.append(r + (128 if len(arr) else 0))
  return arr[::-1]
​
from functools import reduce
def vlq_to_int(lst):
  return reduce(lambda acc, b: acc * 128 + (b & 127), lst, 0)

