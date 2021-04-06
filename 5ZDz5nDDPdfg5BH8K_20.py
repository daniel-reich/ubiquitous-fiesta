
import math
def only_5_and_3(n):
  if n % 5 == 0: return True
  while (math.log(n, 3) % 1 != 0):
    n -= 5
    if n <= 1: return False
  return True

