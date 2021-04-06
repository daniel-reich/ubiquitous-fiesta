
from fractions import gcd as fuck
def lcm(n):
  sol=1
  for i in n:
    sol = (i*sol) // fuck(i,sol)
  return sol

