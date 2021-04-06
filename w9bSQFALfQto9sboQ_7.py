
def gcd(n1, n2):
  return gcd(n2, n1 % n2) if n2 else n1

