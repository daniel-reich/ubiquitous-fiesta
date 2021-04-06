
def mixed_number(frac):
  f = [int(i) for i in frac.split('/')]
  if not f[0]: return '0'
  whole = (abs(f[0])//f[1]) * f[0]//abs(f[0])
  rem = abs(f[0])%f[1]
  return reduce(f[0],f[1]) if not whole else str(whole) if not rem else "{} {}".format(whole, reduce(rem, f[1]))
  
def reduce(n1,n2):
  return '{}/{}'.format(n1//gcd(n2,n1),n2//gcd(n2,n1))
​
def gcd(a,b):
  if b==0:
    return abs(a)
  return gcd(b, a%b)

