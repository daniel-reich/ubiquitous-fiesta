
from math import*
def semiprimes(n):
  l = [i for i in range(2,n) if isprime(i) == True]
  l1 = list(set(i*j for i in l for j in l if i*j < n))
  l2 = [i for i in l1 if not (sqrt(i) - floor(sqrt(i))) == 0]
  return (sorted(l1),sorted(l2))
def isprime(n):
  if (n==1):return False
  elif (n==2):return True
  else:
    for x in range(2,n):
      if(n % x==0):
        return False
    return True

