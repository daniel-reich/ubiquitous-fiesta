
primes = []
def sum_prime(lst):
  def is_prime(num):
    if num >= 2:
      for n in range(2, num):
        if num%n==0:
          return False
      return True
    return False
  
  if len(primes) != 0:
    mp = max(primes)
  else:
    mp = 0
  
  if max(lst) > mp:
    for n in range(mp+1, max(lst)):
      if is_prime(n) == True:
        primes.append(n)
  
  prime_factors = {}
  
  for prime in primes:
    
    for num in lst:
      if prime > num:
        continue
      if num % prime == 0:
        if prime not in prime_factors.keys():
          prime_factors[prime] = [num]
        else:
          prime_factors[prime].append(num)
  
  tr = []
  print(primes)
  for prime in sorted(list(prime_factors.keys())):
    tr.append('({} {})'.format(prime, sum(prime_factors[prime])))
  
  return ''.join(tr)

