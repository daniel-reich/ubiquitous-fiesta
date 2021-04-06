
def filter_primes(num):
  return [i for i in num if prime(i)]
​
def prime(n):
  for i in range(2,n):
    if n%i == 0:
      return False
  return n != 1

