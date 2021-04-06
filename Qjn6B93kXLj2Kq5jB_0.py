
from fractions import gcd
​
def simplify_frac(f):
  n,d = [int(i) for i in f.split('/')]
  return '/'.join(str(i//gcd(n,d)) for i in (n,d))

