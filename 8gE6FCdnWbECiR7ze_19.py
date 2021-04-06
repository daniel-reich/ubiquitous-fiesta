
def isPrime(n):
  if n < 2:
    return False
  else:
    for i in range(2, n):
      if n % i == 0:
        return False
    return True
​
def factors(n):
  return [i for i in range(2, n+1) if n % i == 0]
  
def primeFactors(n):
  p_facts = []
  while n != 1:
    for factor in factors(n)[::-1]:
      if isPrime(factor):
        p_facts.append(factor)
        n = int(n/factor)
  return p_facts
  
def digitalRoot(n):
  dR = 0
  while n != 0:
    dR += (n % 10)
    n //= 10
  return dR
  
def isSmith(n):
  sum = 0
  for prime in primeFactors(n):
    sum += digitalRoot(prime)
  return sum == digitalRoot(n) and not isPrime(n)
​
def smith_type(n):
  if isPrime(n):
    return "Trivial Smith"
  elif isSmith(n) and isSmith(n-1):
    return "Oldest Smith"
  elif isSmith(n) and isSmith(n+1):
    return "Youngest Smith"
  elif isSmith(n):
    return "Single Smith"
  else:
    return "Not a Smith"

