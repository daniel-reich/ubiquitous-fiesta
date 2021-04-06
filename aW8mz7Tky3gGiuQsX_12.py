
def primes(n):
  res = []
  while n > 1:
    for x in range(2, n + 1):
      if n % x == 0:
        n = int(n/x)
        res.append(x)
        break
  return res
​
def is_powerful(n):
  ps = primes(n)
  return all(ps.count(p) > 1 for p in ps)

