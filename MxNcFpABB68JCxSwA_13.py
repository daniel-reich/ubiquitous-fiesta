
def legendre(p, n):
  return sum([n//(p**i) for i in range(1,n//p) if n>=p**i])

