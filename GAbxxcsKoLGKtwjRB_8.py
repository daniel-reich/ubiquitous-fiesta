
def isPrime(num):
  divisors = 0
  for i in range(1,num+1):
    if num%i == 0:
      divisors += 1
  if divisors == 2:
    return True
  else:
    return False
​
def sum_primes(lst):
  if len(lst) == 0:
    return None
  sum = 0
  for e in lst:
    if isPrime(e):
      sum += e
  return sum

