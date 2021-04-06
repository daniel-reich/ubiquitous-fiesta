
from math import sqrt
​
def is_prime(n: int) -> bool:
  if n < 2:
    return False
  if n in (2, 3, 5):
    return True
  for p in (2, 3, 5):
    if n % p == 0:
      return False
  for i in range(6, int(sqrt(n)), 6):
    if n % (i + 1) == 0 or n % (i + 5) == 0:
      return False
  return True
​
def cuban_prime(n: int) -> str:
  if (sqrt((n - 1/4) / 3) - 1/2).is_integer() and is_prime(n):
    return '{} is cuban prime'.format(n)
  else:
    return '{} is not cuban prime'.format(n)

