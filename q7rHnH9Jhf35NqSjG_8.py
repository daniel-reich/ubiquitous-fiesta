
import math
def trailing_zeros(n):
  if n == 0:
    return 0
  return math.floor(n/5) + trailing_zeros(math.floor(n/5))

