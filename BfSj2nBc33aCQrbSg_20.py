
import math
​
def is_prime(n):
  if n < 2:
    return False
  sqrt = math.floor(math.sqrt(n))
  for i in range(2, sqrt + 1):
    if n % i == 0:
      return False
  return True
​
def is_truncatable(n, slc):
  if '0' in str(n):
    return False
  while True:
    if not is_prime(n):
      return False
    if n < 10:
      break
    n = int(str(n)[slc])
  return True
​
def truncatable(n):
  is_left = is_truncatable(n, slice(1, None))
  is_right = is_truncatable(n, slice(None, -1))
  
  if is_left and is_right:
    return "both"
  elif is_left:
    return "left"
  elif is_right:
    return "right"
  else:
    return False

