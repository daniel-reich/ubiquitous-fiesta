
def gcd(n1, n2):
  s = min(n1, n2)
  l = max(n1, n2)
  while s != 0:
    s, l = l % s, s
  return l

