
def gcd(a,b):
  return b if a == 0 else gcd(b%a,a)
​
def simplify_frac(f):
  a,b = (int(e) for e in f.split('/'))
  g = gcd(a,b)
  return str(a//g) + '/' + str(b//g)

