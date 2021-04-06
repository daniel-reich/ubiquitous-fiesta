
import math
def prime(x):
  for i in range (2, 1+ int(math.sqrt(x))):
    if x % i == 0:
      return 0
  return 1

