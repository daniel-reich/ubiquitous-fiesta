
from math import sqrt
​
def prime(x):
  for i in range(3, int(sqrt(x)) + 1, 2):
    if not x % i:
      return False
  return True

