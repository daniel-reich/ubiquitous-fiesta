
from fractions import Fraction
def farey(n):
  return ['0/1'] + list(map(Fraction.__str__, sorted(set([Fraction(b,a) for a in range(2, n+1) for b in range(1, a)])))) + ['1/1']

