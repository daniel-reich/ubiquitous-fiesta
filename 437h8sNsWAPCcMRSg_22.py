
def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
​
def product_of_primes(num):
​
  for i in range(2,num):
    if num % i == 0:
      j = num // i
      if is_prime(j) and is_prime(i):
        return True 
    
  return False

