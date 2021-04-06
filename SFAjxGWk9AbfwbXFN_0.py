
def primes_below_num(n):
  return [i for i in range(2,n+1) if prime(i)]
  
def prime(n):
  for i in range(2,n):
    if n%i == 0:
      return False
  return True

