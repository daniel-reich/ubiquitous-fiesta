
import math
def is_heteromecic(n):
  for k in range(1, int(math.sqrt(n))+1):
    if n-k == k**2:
      return True
  if n==0:
    return True
  else:
    return False

