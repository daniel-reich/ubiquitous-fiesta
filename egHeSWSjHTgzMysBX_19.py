
from fractions import Fraction
def half_a_fraction(fract):
  x = Fraction(fract)
  y = x * Fraction(1,2)
  z = '{}/{}'.format(y.numerator,y.denominator)
  return z

