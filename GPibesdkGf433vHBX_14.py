
import math
import itertools
​
def goldbach_conjecture(n):
  for i in range(n):
    if is_prime(i):
      for j in range(n-i,n):
        if is_prime(j):
          if i + j == n:
            return [i,j]
  
  
  
def is_prime(x):
  if x == 1:
    return False
  if x == 2 or x == 3 or x == 5:
    return True
  elif x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
    return False
  else:
    for i in range(2,int(math.sqrt(x))+1):
      if x % i == 0:
        return False
    return True

