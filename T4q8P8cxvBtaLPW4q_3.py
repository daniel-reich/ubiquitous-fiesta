
def extract_primes(n):
  return sum(([k] * str(n).count(str(k)) for k in crible(n+1)), [])
  
def crible(n):
  s = [None] * n
  for i in range(2, n):
    if s[i] is None:
      yield i
      for k in range(2*i, n, i):
        s[k] = False

