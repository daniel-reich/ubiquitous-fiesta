
def is_prime(num):
  for factor in range(2,num):
    if num%factor==0:
        return False
  return True
      
primes = [entry for entry in range(2,1000) if is_prime(entry)]
print(primes)
​
​
def divisible(num):
  for prime in primes:
      divided = num/prime
      if int(divided) == divided:
        return divided
​
  return "not divisible"
​
def product_of_primes(num):
  print(num)
  if divisible(num)=="not divisible":
    return False
  else:
    print(divisible(num))
    if divisible(num) in primes:
      return True
  
  return False

