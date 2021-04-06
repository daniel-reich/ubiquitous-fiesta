
def simplify(txt):
  from fractions import gcd
  a, b = txt.split('/')
  a, b = int(a), int(b)
  c = gcd(a, b)
  a, b = int(a / c), int(b / c)
  return str(a) if b == 1 else str(a) + "/" + str(b)

