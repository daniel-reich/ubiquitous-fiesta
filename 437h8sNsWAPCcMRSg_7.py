
def product_of_primes(num):
  import math as m
  prime_factors=[]
  while num % 2 == 0:
    num = num / 2
    prime_factors.append(2)
  for i in range(3,int(m.sqrt(num)+1),2):
    while num % i == 0:
      num = num / i
      prime_factors.append(i)
  if num > 2:
    prime_factors.append(num)
  if len(prime_factors) == 2:
    return True
  else:
    return False

