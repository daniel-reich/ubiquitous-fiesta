
def sexy_primes(n, limit):
  limit = prime_list(limit)
  result = []
  for i in limit:
    if n == 2 and i+6 in limit:
      result.append((i,i+6))
    elif n == 3 and i+6 in limit and i+12 in limit:
      result.append((i,i+6,i+12))
  return result
  
def prime_list(n):
  return [x for x in range(2, n+1) if len([y for y in range(2,x+1) if x % y == 0]) == 1]

