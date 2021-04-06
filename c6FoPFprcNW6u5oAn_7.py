
from fractions import Fraction
from itertools import combinations as com
def farey(n):
  fractions = list(com([x for x in range(1,n+1)],2))
  Frac = []
  for n,d in fractions:
    if Fraction(n,d) not in Frac:
      Frac.append((Fraction(n,d)))
  Frac.sort()
  Frac.append("1/1")
  return ["0/1"] + [str(x) for x in Frac]

