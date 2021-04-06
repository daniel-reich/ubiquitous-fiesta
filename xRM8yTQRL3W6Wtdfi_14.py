
def quartic_equation(a, b, c):
  if a==0:
    if b==0: return float('Inf') if c==0 else 0
    if c>0: return 0
    return 1 if c==0 else 2
  
  req=(b/a/2)**2-c/a
  if req<0: return 0
  return sum ([1 if x==0 else 2 for x in (-b/a/2+req**0.5,-b/a/2-req**0.5 ) if x>=0])

