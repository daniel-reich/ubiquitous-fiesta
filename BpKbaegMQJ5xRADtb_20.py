
import numpy as np
from bisect import insort
​
def primes(n):
  flags = np.ones(n,dtype=bool)
  flags[0]=flags[1]=False
  m = int(np.sqrt(n))+1
  for i in range(2,m):
    if flags[i]:
      flags[i*i::i] = False
  return np.flatnonzero(flags)
  
def is_unprimeable(num):
  num = str(num)
  pr = primes(10**len(num))
  if int(num) in pr:
    return "Prime Input"
  res = []
  for i in range(len(num)):
    for j in range(10):
      tmp = int(num[:i]+str(j)+num[i+1:])
      if tmp in pr:
        res.append(tmp)
  return sorted(res) if res else 'Unprimeable'

