
from fractions import gcd
def lcm(num):
  a = num  
  lcm = a[0]
  for i in a[1:]:
    lcm = lcm*i/gcd(lcm, i)
  return lcm

