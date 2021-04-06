
from functools import reduce
def is_prime(n):
  ret=True if n>1 else False
  for i in range(2,n//2+1):
    if n%i==0:
      ret=False
      break
  return ret
def primes_factorization(n,pl):
  f=[0]*len(pl)
  for i in range(len(pl)):
    n1=n
    while n1%pl[i]==0:
      f[i]+=1
      n1=n1//pl[i]
  return f
def lcm(l):
  nl=list(range(2,max(l)+1))
  pl=list(filter(is_prime,nl))
  print(pl)
  pf=[primes_factorization(x,pl) for x in l]
  print(pf)
  pft=[list(x) for x in zip(*pf)]
  print(pft)
  pftm=list(map(lambda x: max(x),pft))
  print(pftm)
  pftmp=[pl[x]**pftm[x] for x in range(len(pl))]
  print(pftmp)
  return reduce(lambda x,y: x*y, pftmp, 1)

