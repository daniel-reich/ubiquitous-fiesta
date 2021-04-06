
from math import floor
def is_prime(n):
  if n < 2: return False
  for i in range(2, floor(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
  
def is_unprimeable(num):
  if is_prime(num): return "Prime Input"
  res = []
  num = list(str(num))
  for pv, orig in enumerate(num):
    for digit in "0123456789":
      num[pv] = digit
      val = int(''.join(num))
      if is_prime(val):
        res.append(val)
    num[pv] = orig
  if res:
    res.sort()
    return res
  else:
    return 'Unprimeable'

