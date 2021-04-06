
def lcm(n1, n2):
  if n2>n1: 
    n1,n2 = n2,n1
  return next(n2*x for x in range(1, n1*n2) if not (n2*x) % n1)

