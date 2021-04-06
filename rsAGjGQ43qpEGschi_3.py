
from numpy import*
def newton_raphson(c):
  p=poly1d(c)
  q=p.deriv()
  e,x,a=0.001,1,0
  while abs(p(x))>e:
    k=q(a)
    if k!=0:x=a-p(a)/k
    a=x-0.001
  return round(x,3)

