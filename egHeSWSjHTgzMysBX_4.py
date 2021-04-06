
from fractions import Fraction
def half_a_fraction(fract):
  a = fract.split('/')
  n1 = int(a[0])
  n2 = int(a[1]) * 2
  return str(Fraction(n1,n2))

