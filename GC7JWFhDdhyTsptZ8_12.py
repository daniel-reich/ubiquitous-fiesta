
def sexy_primes(n, limit):
  is_prime = lambda n: all(n%i for i in range(2,1+int(n**(.5)))) if n>1 else False
​
  return [tuple(i+6*r for r in range(n)) for i in range(2,limit-6*n+6) if all(is_prime(k) for k in (i+6*r for r in range(n)))]

