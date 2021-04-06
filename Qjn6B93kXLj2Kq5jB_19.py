
from fractions import Fraction
def simplify_frac(f):
  a = f.split('/')
  return str(Fraction(int(a[0]), int(a[1])))

