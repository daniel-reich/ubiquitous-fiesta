
from fractions import gcd
​
def smallest(n):
   lcm = 1
   for i in range(1, n+1):
       lcm = (lcm * i)//(gcd(int(lcm), i))
   return int(lcm)

