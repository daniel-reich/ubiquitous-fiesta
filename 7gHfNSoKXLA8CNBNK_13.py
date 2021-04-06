
from fractions import Fraction
def den(d):
  return list(map(lambda x: Fraction(x,d),range(1,d)))
def sim_prop_frac(max_den):
  fractions = []
  for i in range(2,max_den+1):
    fractions.extend(den(i))
  return len(set(fractions))

