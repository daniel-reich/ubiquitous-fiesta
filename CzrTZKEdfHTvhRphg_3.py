
def gcd(a,b):
  return gcd(b,a%b) if b else a
  
def mixed_number(frac):
  x, y = map(int, frac.split('/'))
  d = gcd(x,y)
  x //= d
  y //= d
  w = abs(x)//y
  n = abs(x)%y
  
  s = "-" if x<0 else ""
  
  if not n:
    return s + str(w)
  elif not w:
    return s + str(n)+'/'+str(y)
  return s + str(w) + " " + str(n)+'/'+str(y)

