
def primes_below_num(n):
  return [i for i in range(1, n + 1) if is_prime(i)]
​
def is_prime(n):
  return sum(not n % i for i in range(1, n)) == 1

