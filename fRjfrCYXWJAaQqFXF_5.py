
def primorial(n):
  prime = 0
  num = 2
  prod = 1
  while(prime < n):
    if isPrime(num):
      prod *= num
      prime += 1
    num += 1
  return prod
​
​
def isPrime(num):
  for i in range(2,num):
     if (num % i) == 0:
      return False
  return True

