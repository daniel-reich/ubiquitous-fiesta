
def prime_in_range(n1, n2):
  return any(isPrime(n) for n in range(n1, n2+1))
  
def isPrime(N):
  return not any(not N%n for n in range(2, int(N**0.5)+1))

