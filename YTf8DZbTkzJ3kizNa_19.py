
import math
​
def isPrime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if not n%i: return False
  return True
​
def moran(n):
  divisor=0
  for x in str(n):
    divisor+=int(x)
  if not n%divisor:
    if isPrime(n//divisor): return 'M'
    return 'H'
  return 'Neither'

