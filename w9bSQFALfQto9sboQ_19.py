
def gcd(n1, n2):
  gcd=1
  for x in range(1,min(n1,n2)+1):
    if n1%x==0 and n2%x==0: gcd=x
  return gcd

