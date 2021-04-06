
import math
​
def primorial(n):
  count = 0
  increment = 2
  total = 1
  while count != n:
    if is_prime(increment):
      total = total * increment
      count += 1
      increment += 1
    else:
      increment += 1
  return total
  
  
def is_prime(n):
  if n == 2 or n == 3 or n == 5:
    return True
  elif n < 2:
    return False
  elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
    return False
  else:
    for i in range(2,int(math.sqrt(n))+1):
      if n % i == 0:
        return False
    return True

