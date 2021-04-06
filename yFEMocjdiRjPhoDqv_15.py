
is_prime = lambda n: all(n % i for i in range(2, n)) and n > 1
def prime_in_range(n1, n2):
  return any(is_prime(n) for n in range(n1, n2 + 1))

