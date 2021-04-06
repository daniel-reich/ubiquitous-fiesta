
import math
​
​
def logarithm(base, num):
  if base <= 1 or num <= 1:
    return 'Invalid'
  return math.log(num, base)

