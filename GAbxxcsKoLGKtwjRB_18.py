
def is_prime(n):
  if n == 1:
    return False
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      return False
  return True
​
def sum_primes(lst):
  prime_lst = list(filter(is_prime, lst))
  if prime_lst == []:
    return None
  return sum(prime_lst)

