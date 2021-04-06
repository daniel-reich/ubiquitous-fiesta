
def gcd(l, m):
  if l < m: l,m = m,l
  while m > 0:
    l, m = m, l % m
  return l
  
def lcm(n1, n2):
  return n1 * n2 // gcd(n1, n2)

