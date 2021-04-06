
import math
​
def isPrime(n):
  for x in range(1, int(math.sqrt(n)+1)):
    if (n%x == 0) and (x!=1) or (n==1):
      return False
  return True
​
def lcm(n1, n2):
  largest = max(n1, n2)
  least = min(n1, n2)
  intersection = 1
  exit = False
  while least != 1 and exit==False:
    for x in range(1, int(least+1)):
      if isPrime(x) and largest%x==0 and least%x==0:
        largest /= x
        least /= x
        intersection *= x
        break
      if x == least:
        exit = True
  return int(n1*n2/intersection)

