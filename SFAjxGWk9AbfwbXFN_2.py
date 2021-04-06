
def primes_below_num(n):
  def is_prime(n):
    for num in range(2, n):
      if n%num == 0:
        return False
    return True
  
  primes = []
  
  for num in range(2, n+1):
    p = is_prime(num)
    if p == True:
      primes.append(num)
  
  return primes

