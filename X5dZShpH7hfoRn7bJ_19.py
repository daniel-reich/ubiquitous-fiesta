
def c_fuge(n, k):
  lst = prime_facts(n)
  poss = {0}
  for p in lst:
    poss = {a+b for a in poss for b in range(0,n+1,p) if a+b<=n}
  return k in poss and n-k in poss  
​
def prime_facts(n):
  ans = []
  for p in range(2,n+1):
    if n%p == 0 and all(p%k for k in ans): ans+=[p]
  return ans

