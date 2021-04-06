
def lcm(n1, n2):
  r=n1*n2
  while n2:
    n1,n2=n2,n1%n2
  return r//n1

