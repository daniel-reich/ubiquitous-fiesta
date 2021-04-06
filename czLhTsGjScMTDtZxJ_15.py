
def is_prime(n):
  if n%2==0:return False
  for i in range(3,n):
    if n%i==0:return False
  return True
def primorial(n):
  ans=1
  primes=[2]
  check=3
  while True:
    if len(primes)==n:
      for i in primes:
        ans*=i
      return ans
    else:
      if is_prime(check):
        primes.append(check)
        check+=1
      else:check+=1

