
import math
def only5and3(n):
  if math.log(n,3)%1 == 0 or n%5 == 0:
    return True
  else:
    n -= 5
    if 3 < n < 5 or n < 3:
      return False
    return only5and3(n)

