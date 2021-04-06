
from fractions import Fraction
def mixed_number(frac):
  sgn = lambda n: 0 if n == 0 else n // abs(n)
  f = Fraction(frac)
  w, r = divmod(abs(f.numerator), f.denominator)
  w *= sgn(f.numerator)
  if abs(w) > 0:
    return "{} {}/{}".format(w, r, f.denominator) if r > 0 else str(w)
  return str(f)

