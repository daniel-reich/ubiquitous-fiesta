
from fractions import*
def sim_prop_frac(n):
  l = {Fraction(i,j) for i in range(1,n+1) for j in range(1,i+1)}
  return len(l) -1

