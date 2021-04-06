
def sexy_primes(n, limit):
  res=[]
  for i in range(limit-6*(n-1)):
    if isprime(i):
      if all([isprime(6*j+i) for j in range(1,n)]):
        res+=[tuple(6*j+i for j in range(n))]
  return res
  
def isprime(num):
  return num>1 and all([num%i for i in range(2,num//2+1)])

