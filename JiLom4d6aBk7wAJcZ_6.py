
import math
​
def is_sastry(n):
  res = str(n) + str(n + 1)
  resn = math.sqrt(int(res))
  return resn.is_integer()

