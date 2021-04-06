
def gcd(x,y):
  while(y): x, y = y, x%y
  return x
​
def fractions(d):
  p_ent = d[:d.index('.')]
  p_dec = d[d.index('.')+1:d.index('(')]
  rep = d[d.index('(')+1:d.index(')')]
​
  f = [int(rep), 10**len(p_dec)*(10**(len(rep))-1)]
  f[0]+=int(p_ent)*f[1]
  if len(p_dec): f[0]+=int(p_dec)*(10**(len(rep))-1)
​
  g=gcd(f[0],f[1])
  f=[f[0]//g,f[1]//g]
  
  return str(f[0])+'/'+str(f[1])

