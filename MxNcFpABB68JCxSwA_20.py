
import math
def legendre(p, n):
  return sum(int(n/(p**x)) for x in range(1,int(math.log(n,p)) + 1))

