
from math import sqrt, floor
def is_prime(n):
  if n < 2: return False
  if n < 4: return True
  if n % 2 == 0: return False
  return all(bool(n % f) for f in range(3, int(sqrt(n)) + 1, 2))
​
def is_exactly_three(n):
  root2 = floor(sqrt(n))
  return root2 * root2 == n and is_prime(root2)

