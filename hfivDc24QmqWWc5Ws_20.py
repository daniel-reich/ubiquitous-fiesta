
def eratosthenes(num):
  primes = []
  for i in range(1,num+1):
    if len([x for x in range(1,i//2+1) if i%x==0]) == 1:
      primes.append(i)
      
  return primes

