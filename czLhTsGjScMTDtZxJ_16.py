
import numpy as np
from functools import reduce
def sieve(n):
  fl = np.ones(n,dtype=bool)
  fl[0] = fl[1] = False
  for i in range(2,int(n**0.5)+1):
    if fl[i]:
      fl[i*i::i] = False
  return np.flatnonzero(fl)
  
def primorial(n):
  x = 20
  pr = sieve(x)
  while len(pr) < n:
    x *= 5
    pr = sieve(x)
  return reduce(lambda x,y:x*y, pr[:n])

