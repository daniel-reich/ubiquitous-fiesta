
from fractions import Fraction
def simplify_frac(f):
  return str(Fraction(eval(f)).limit_denominator())

