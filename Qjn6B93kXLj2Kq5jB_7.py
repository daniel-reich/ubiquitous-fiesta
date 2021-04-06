
from fractions import Fraction
def simplify_frac(f):
  f = Fraction(f)
  num = str(f.numerator)
  den = str(f.denominator)
  return num + '/' + den

