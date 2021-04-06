
def gcd(a, b):
  if   a == 0: return b
  elif b == 0: return a
  x = max(a, b)
  y = min(a, b)
  return gcd(y, x % y)

