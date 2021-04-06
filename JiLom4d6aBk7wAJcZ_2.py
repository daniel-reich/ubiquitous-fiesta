
import math
def is_sastry(n):
  b = int(str(n) + str(n + 1))
  if math.sqrt(b) % 1 == 0:
    return True
  else:
    return False

