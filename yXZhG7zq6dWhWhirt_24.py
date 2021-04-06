
def is_prime(n):
  if (n==1):
    return False
  for i in range(2,round(n**(0.5))+1):
    if i!=n and (n%i)==0:
      return False
  return True
  
def filter_primes(num):
  return [n for n in num if is_prime(n)]

