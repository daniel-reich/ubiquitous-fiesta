
import math
def i_sqrt(n):
  if n < 0:
    return "invalid"
  elif n < 2:
    return 0
  else:
    return i_sqrt(math.sqrt(n)) + 1

