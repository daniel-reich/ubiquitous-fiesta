
def sexy_primes(n, limit):
  primes = []
  
  for i in range(1, limit):
    no_prime = False
    for p in primes:
      if p != 1 and i % p == 0:
        no_prime = True
        break
    
    if no_prime:
      continue
    else:
      primes.append(i)
  matches = []
  additions = 6 * (n -1) + 1
  
  for i in range(0, len(primes)):
    p = primes[i]
    if p == 1:
      continue
    current = []
    for i in range(p, (p + additions), 6):
      if i in primes:
        current.append(i)
  
    if len(current) == n:
      matches.append(current)
  result = []   
  for m in matches:
    result.append(tuple(m))
  return result

