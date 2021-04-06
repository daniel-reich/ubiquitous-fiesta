
def product_of_primes(num):
  import math
  primes = []
  n = num
  while n % 2 == 0:
    primes.append(2)
    n = n / 2
  for i in range(3, num, 2):
    while n%i==0:
      primes.append(i)
      n = n/i
  for idx,i in enumerate(primes):
    for j in range(idx):
      if i * primes[j] == num:
        return True
  return False

