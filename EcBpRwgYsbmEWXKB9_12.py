
import math
def prime(x):
  if x < 2:
    return False
  if x == 2 or x == 3 or x == 5:
    return True
  if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
    return False
  else:
    for i in range(6,int(math.sqrt(x))+1):
      if x % i == 0:
        return False
    return True

