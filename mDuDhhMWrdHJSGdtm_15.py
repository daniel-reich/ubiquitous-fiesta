
def divisible(n):
  return (n**0.5) % 1 == 0 and isPrime(n)
def isPrime(n):
  if n == 1:
    return False
  else:
    for i in range(2,int(n**0.5)):
      if n%i == 0:
        return False
  return True

