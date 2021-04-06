
from fractions import Fraction
def parallel_resistance(lst):
  total = sum([Fraction(1,i) for i in lst])
  return round(total.denominator/total.numerator, 1)

