
def prime_gaps(g, a, b):
  pp = None
  for x in range(a, b+1):
    if is_prime(x):
      if pp and x-pp == g:
        return [pp, x]
      pp = x
  return None
  
def is_prime(n):
  if n < 4 or n%2 == 0: return n == 2 or n == 3
  return all(bool(n%i) for i in range(3, int(1 + n**0.5), 2))

