
from fractions import Fraction
def half_a_fraction(fract):
  n, d = fract.split("/")
  return str(Fraction(int(n), int(d)) * Fraction(1,2))

