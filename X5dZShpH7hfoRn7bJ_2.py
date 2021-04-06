
import itertools as it
​
def prime(n):
  if n<2: return False
  return not [i for i in range(2,(n//2)+1) if not n%i]
def p_fac(n):
  if n<2: return []
  return [i for i in range(2,n+1) if not n%i and prime(i)]
​
def c_fuge(n, k):
  pf = p_fac(n)
  if n==1 or k==1: return False
  if n==k : return True
  check=[0,0]
  for i in range(1, n//pf[0]):
      for j in list(it.combinations_with_replacement(pf,i)):
          if sum(j)==k:
              check[0]+=1
          if sum(j)==n-k:
              check[1]+=1
  return check.count(0)==0

