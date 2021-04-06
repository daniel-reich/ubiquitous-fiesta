
def is_prime(num):
  for i in range(2, int(num ** 0.5)+1):
    if num % i == 0:
      return False
  else:
    return True
​
def primes_below_num(n):
  return [num for num in range(2,n+1) if is_prime(num)]

