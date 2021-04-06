
def simplify(txt):
  fst, snd = txt.split('/')
  fst, snd = int(fst), int(snd)
  
  if fst % snd == 0:
    return str(fst // snd)
    
  g = gcd(fst, snd)
  return str(fst // g) + '/' + str(snd // g)
​
def gcd(x, y):
  while (y):
    x, y = y, x % y
  
  return x

