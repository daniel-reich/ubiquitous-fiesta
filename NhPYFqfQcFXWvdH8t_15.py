
from fractions import gcd
def mod_inv(n, m):
  if gcd(n,m)-1:
    return False
  for i in range(1,m):
    if not (n*i)%m-1:
      return i

