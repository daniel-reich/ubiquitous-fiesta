
from fractions import Fraction
​
def _get_decimal(frac):
  parts = frac.split(".")
  return int(parts[0], 2) + int(parts[1], 2) / 2 ** len(parts[1])
​
def binary_sum(lst):
  frac = Fraction(sum(_get_decimal(f) for f in lst))
  if frac.numerator > frac.denominator and frac.denominator != 1:
    num = frac.numerator // frac.denominator
    return "{} {}".format(num, Fraction(frac.numerator % frac.denominator, frac.denominator))
  return str(frac)

