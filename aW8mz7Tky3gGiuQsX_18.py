
from math import sqrt
def isPrime(x):
  for i in range(2, int(sqrt(x))+1):
    if x%i==0:return False
  return True
def is_powerful(n):
  primefactors = [i for i in range(2, int(sqrt(n))) if n%i==0 and isPrime(i)]
  for p in primefactors:
    if n%(p**2)!=0:
      return False
  return True

