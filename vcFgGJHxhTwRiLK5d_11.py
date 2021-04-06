
from decimal import *
getcontext().prec = 50
def gcd(x, y):
  x, y = max(x,y), min(x,y)
  while(y): 
    x, y = y, x % y 
  return x 
​
def smallest(n):
  res = Decimal(1)
  for i in range(2,n+1):
    res = res*i/gcd(res, i)
  return res

