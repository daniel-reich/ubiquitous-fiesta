
def smith_type(n):
  if smith(n):
    if smith(n+1): return 'Youngest Smith'
    if smith(n-1): return 'Oldest Smith'
    return 'Single Smith'
  if len(pri_fact(n)) == 1: return 'Trivial Smith'
  return 'Not a Smith'
  
def smith(n):
  f = pri_fact(n)
  return len(f) > 1 and dig_root(n) == dig_root(sum(f))
  
def pri_fact(n):
  factors = []
  for i in range(2, n+1):
    while not n % i:
      factors += [i]
      n //= i
  return factors
  
def dig_root(n):
  return n if n < 10 else dig_root(sum(int(d) for d in str(n)))

