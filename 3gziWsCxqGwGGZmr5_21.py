
import numpy as np
def fat_prime(a, b):
  n=max(a,b)
  flags = np.ones(n, dtype=bool)
  flags[0]=flags[1]=False
  m = int(np.sqrt(n))+1
  for i in range(2,m):
    if flags[i]:
      flags[i*i::i] = False
  return np.flatnonzero(flags)[-1]

