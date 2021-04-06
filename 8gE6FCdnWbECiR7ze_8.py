
def smith_type(n):
  root = lambda x: root(x % 9) if x > 9 else x
  prime = lambda x: x > 1 and all(x % m for m in range(2, int(x**0.5)+1))
  def factors(k, f=list()):
    if k < 2: return f
    if prime(k): return f+[k]
    for i in range(2, k//2+1):
      if prime(i) and not (k % i):
        return factors(k//i, f+[i])
  if prime(n): return 'Trivial Smith'
  if n == 1 or n % 9 != root(sum(factors(n))): return 'Not a Smith'
  return '{} Smith'.format('Youngest' if not prime(n+1) and (n+1) % 9 == root(sum(factors(n+1)))
    else 'Oldest' if not prime(n-1) and (n-1) % 9 == root(sum(factors(n-1))) else 'Single')

