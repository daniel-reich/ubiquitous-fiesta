
from math import sqrt
​
def is_prime(n):
  if n == 1:
    return False
  for i in range(2,n):
    if n % i == 0:
      return False
  return True
  
def is_unprimeable(num):
  if is_prime(num):
    return "Prime Input"
  else:
    a = str(num)
    primes = list()
    for i in range(len(a)):
      for j in range(10):
        a = list(a)
        a[i] = str(j)
        a ="".join(a)
        if is_prime(int(a)):
          primes.append(int(a))
      a = str(num)
    if 0 in primes: 
      primes.remove(0)
    if len(primes) != 0:
      return sorted(primes)
    else:
      return"Unprimeable"
    
    
    
[137, 2137, 3137, 9137, 5237, 5437, 5737, 5107, 5147, 5167, 5197]
[137, 2137, 3137, 5107, 5147, 5167, 5197, 5237, 5437, 5737, 9137]

