
from decimal import *
def float_sum(A, B):
  if len(str(A))>len(str(B)):
    length=len(str(A))
  else:
    length=len(str(B))
  getcontext().prec=length
  out=float(Decimal(A)+Decimal(B))
  return out

