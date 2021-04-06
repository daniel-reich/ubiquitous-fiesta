
import numpy as np
def sieve(n):
  fl = np.ones(n,dtype=bool)
  fl[0]=fl[1]=False
  for i in range(int(n**0.5)+1):
    if fl[i]:
      fl[i*i::i] = False
  return np.flatnonzero(fl)
def goldbach_conjecture(n):
  if n&1:
    return []
  pr = sieve(n)
  for k in pr:
    if n-k in pr:
      return [k,n-k]

