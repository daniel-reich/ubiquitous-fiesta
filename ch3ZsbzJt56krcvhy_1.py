
from decimal import*
def square_root(n):
  getcontext().prec=42
  x,c=Decimal(n),0 
  while 1: 
      c,r=c+1,Decimal(.5)*(x+(n/x))
      if abs(r-x)<1e-5:return r 
      x=r

