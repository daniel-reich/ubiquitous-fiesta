
def gcd(n1, n2):
  return max([c for c in range(1,min([n1,n2])+1) if n1%c==0 and n2%c==0])

