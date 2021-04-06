
from fractions import gcd
def lcm(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//gcd(lcm,a[i])
  return lcm

