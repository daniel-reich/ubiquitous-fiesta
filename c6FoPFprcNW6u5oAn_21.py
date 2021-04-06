
def gcd(x,y):
  x,y=abs(x),abs(y)
  if x*y==0:
    return x+y
  while y!=0:
    x,y=y,x%y
  return x
def farey(n):
  fl=[(a,b) for b in range(1,n+1) for a in range(0,b+1)]
  flm=list(map(lambda x: (x[0]//gcd(*x),x[1]//gcd(*x)),fl))
  flms=list(sorted(set(flm), key=lambda x: x[0]/x[1]))
  return list(map(lambda x: str(x[0])+'/'+str(x[1]), flms))

