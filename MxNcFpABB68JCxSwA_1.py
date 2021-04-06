
def legendre(p, n):
  import math
​
  return(sum(n//p**i for i in range(1,math.floor(math.log(n,p))+1) ))

