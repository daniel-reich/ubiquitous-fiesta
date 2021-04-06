
from fractions import gcd
def sim_prop_frac(max_den):
  s = set()
  for i in range(2,max_den+1):
    for j in range(1,i):
      if gcd(j,i) == 1:
        s.add('{}/{}'.format(j,i))
  return len(s)

