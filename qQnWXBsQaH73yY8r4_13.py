
import math
def kempner(n):
  #find lowest integer which factorial divides into n 
  if isItPrime(n):
    return n
  else:
    for x in range(1,n+1):
      f=factorial(x)
      if f%n==0:
        return x
        
def factorial(n):
  return n<2 or n*factorial(n-1)
​
def isItPrime(n):
  sq=round(math.sqrt(n)+1)
  for x in range(2,sq):
  
    if n%x==0:
      return False
    
  return True

