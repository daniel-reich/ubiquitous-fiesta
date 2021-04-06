
def sexy_primes(n, limit):
  primes = [x for x in range(limit) if isPrime(x)]
  if n == 2:
    return sexyDoubles(primes)
  elif n == 3:
    return sexyTriples(primes)
​
​
​
​
def isPrime(n):
  return len([i for i in range(1,n+1) if n%i==0])==2
​
def sexyDoubles(lst):
  res = []
  for i in lst:
    for j in lst:
      if j - i == 6 and (i, j) not in res:
        res += [(i,j)]
  return res
def sexyTriples(lst):
  res = []
  for i in lst:
    for j in lst:
      for k in lst:
        if k - j == 6 and j - i == 6 and (i, j, k) not in res:
          res += [(i, j, k)]
  return res

