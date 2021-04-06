
def c_fuge(n, k):
  def prime_finder(n):
    primes = []
​
    for num in range(2, n + 1):
      if len(primes) == 0:
        primes.append(num)
      else:
        prime = True
        for item in primes:
          r = num % item
​
          if r == 0:
            prime = False
            break
        
        if prime == True:
          primes.append(num)
    
    return primes
  def prime_divisors(n, primes):
    
    p_divs = []
​
    for prime in primes:
      r = 0
      while r == 0:
        r = n % prime
​
        if r == 0:
          p_divs.append(prime)
          n = n/prime
    
    return p_divs
  def can_be_added(n, primes):
    
    primes = sorted(primes)
    orig_n = n
​
    m = min(primes)
    
    for prime in primes:
      r = n % prime
​
      if r == 0:
        return True
    for index in range(1, len(primes) + 1):
      prime = primes[-index]
      
      while n >= prime:
        n -= prime
        div = False
        
        for p in primes:
          r = n % p
​
          if r == 0:
            div = n / p, p
        
        if div != False:
          for num in range(0, int(div[0])):
            n -= int(div[1])
        
        
    
    if n == 0:
      return True
    else:
      return False
  
  if n == 1 or k == 1 or k > n:
    return False
  
  pfn = prime_finder(n)
  pdn = prime_divisors(n, pfn)
  pdn = set(pdn)
​
  d = n - k
​
  kadd = can_be_added(k, pdn)
  dadd = can_be_added(d, pdn)
​
  if kadd == True and dadd == True:
    return True
  else:
    return False

