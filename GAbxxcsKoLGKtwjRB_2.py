
def sum_primes(lst):
  isprime = lambda n: n>1 and all(n % i for i in range(2, int(n**0.5)+1))
  return sum(n for n in lst if isprime(n)) or None

