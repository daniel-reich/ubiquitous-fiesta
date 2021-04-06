
import numpy as np
def numpy_sieve(n):
    flags = np.ones(n,dtype=bool)
    flags[0] = flags[1] = False
    m = int(np.sqrt(n))+1
    for i in range(2,m):
        if flags[i]:
            flags[i*i::i] = False
    return np.flatnonzero(flags)
    
def moran(n):
  tot,x,primes = 0,n,numpy_sieve(1000)
  while x:
    x,r = divmod(x,10)
    tot += r
  return 'Neither' if n%tot else 'M' if n/tot in primes else 'H'

