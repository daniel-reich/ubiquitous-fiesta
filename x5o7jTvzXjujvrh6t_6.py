
from math import sqrt
def i_sqrt(n):
  if n > 0:
    count = 0
    while n >= 2:
      count += 1
      n = sqrt(n)
    return count
  return 'invalid'

