
from math import factorial
​
def mod(base, key):
  if base > key:
    base = key
  loop = 1
  key = factorial(key)
  f = 1
  for i in range(1, base):
    f = f * i
    loop += f % key
  return loop % key

