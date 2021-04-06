
def fractions(decimal):
  x1 = 10**(decimal.index('(')-decimal.index('.')-1)
  x2 = 10**(decimal.index(')')-decimal.index('.')-2)
  d = x2-x1
  y1 = int(decimal.replace('.','').split('(')[0])
  y2 = int(decimal.replace('.','').replace('(','').replace(')',''))
  n = y2 - y1
  g = gcd(d,n)
  return str(n//g)+'/'+str(d//g)
  
def gcd(a,b):
  if (b == 0):
    return a
  return gcd(b,a%b)

