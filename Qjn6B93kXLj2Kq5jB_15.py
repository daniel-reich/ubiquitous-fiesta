
def gcd(a, b):
  if b == 0: return a
  return gcd(b, a % b)
def simplify_frac(f):
  num, deno = map(int, f.split('/'))
  g = gcd(num, deno)
  return '{}/{}'.format(num//g, deno//g)

