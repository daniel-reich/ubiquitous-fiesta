
import numpy as np
def primorial(n):
  i = 2
  lst = []
  while len(lst) < n:
    if is_prime(i):
      lst.append(i)
    i += 1
  return np.prod(lst)
    
​
def is_prime(n):
    if n <= 1:
      return n > 1
    true = []
    for i in range(2, n):
      true.append(n % i != 0)
    return all(true)

