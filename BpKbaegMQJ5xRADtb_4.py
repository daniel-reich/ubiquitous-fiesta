
def is_unprimeable(n):
  def is_prime(n):
    return all(n%i for i in range(2,int(n**(.5)+1))) if n-1 else False
  
  if is_prime(n):
    return "Prime Input"
  
  sn = str(n)
  
  numsts = [sn[:i] + d + sn[i+1:] for i in range(len(sn)) for d in "0123456789"]
  primes = [int(m) for m in numsts if is_prime(int(m)) and int(m)]
  
  if primes:
    return sorted(primes)
  return "Unprimeable"

