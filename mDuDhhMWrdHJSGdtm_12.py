
import math
​
def is_prime(n):
​
  factors = 0
​
  for i in range(1,n+1):
    if n%i==0:
      factors += 1
  if factors == 2:
    return True
  else:
    return False
​
def is_exactly_three(n):
  root = float(math.sqrt(n))
  if n == 1:
    return False
  elif root.is_integer():
    return is_prime(int(root))
  else:
    return False

