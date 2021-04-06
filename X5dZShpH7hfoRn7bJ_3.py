
import itertools
def c_fuge(n, k):
  if n <= 1 or k <= 1 or k > n:
    return False
  elif n == k:
    return True
  else:     
    factors = get_prime_factors(n)
    possible_sums = set(sum(k) for i in range(1,len(factors)+1) for k in itertools.permutations(factors,i))
    if k in factors or n-k in factors or k in possible_sums:
      return True
  return False
  
def get_prime_factors(n):
  factors = []
  for i in range(2,n):
    while not n%i:
      factors.append(i)
      n //= i
  return factors

