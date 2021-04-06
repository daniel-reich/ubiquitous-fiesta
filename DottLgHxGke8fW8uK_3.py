
from math import*
def nPr(n,r):
  p=1
  for x in range(n-r+1,n+1):p*=x
  return p
nCr=lambda n,r:nPr(n,r)/factorial(r)if n-r>r else nPr(n,n-r)/factorial(n-r)

