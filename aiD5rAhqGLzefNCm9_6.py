
from random import randrange
def is_prime(n):
  if n in (0,1,4,6,8,9): return False
  if n in (2,3,5,7): return True
  s, d = 0, n-1
  while not d%2:
    d >>= 1
    s += 1
  for i in range(8):
    a = randrange(2, n)
    if test_composite(a, d, n, s): return False
  return True
​
def test_composite(a, d, n, s):
  if pow(a, d, n) == 1: return False
  for i in range(s):
    if pow(a, 2**i * d, n) == n-1: return False
  return True

