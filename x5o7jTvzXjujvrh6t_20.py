
import math
def i_sqrt(n):
  count = 0
  if n < 0:
    return "invalid"
  elif n < 2:
    return 0
  while n >= 2:
    n = math.sqrt(n)
    count += 1
  return count

