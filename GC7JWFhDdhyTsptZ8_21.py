
def sexy_primes(n, limit):
  lst=[]
  for x in range(3,limit):
    if is_prime(x):
      tmp=[x+(i*6) for i in range(n)]
      if all([is_prime(i) and i<limit for i in tmp]): lst.append(tuple(tmp))
  return lst
        
  
def is_prime(n):
  return all([n%x!=0 for x in range(2,n)])

