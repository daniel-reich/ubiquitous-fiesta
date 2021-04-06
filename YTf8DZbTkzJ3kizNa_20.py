
import math
def moran(n):
  print(n)
  sum_d = sum_digits(n)
  print(sum_d)
  if n%sum_d == 0:
    print(int(n/sum_d))
    if isprime(int(n/sum_d)):
      return "M"
    else:
      return "H"
  else:
    return "Neither"
​
def isprime(n):
  for i in range(2,round(math.sqrt(n))+1):
    
    if n%i == 0:
      return False
  return True
      
def sum_digits(n):
  sum_dig = 0
  while(n > 0):
    sum_dig+=n%10
    n = int(n/10)
  return sum_dig

