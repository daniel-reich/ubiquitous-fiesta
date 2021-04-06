
def prime_factorization(n):
  i = 2
  out = []
  while i <= n:
    if n % i == 0:
      out.append(i)
      n /= i
    else:
      if i == 2:
        i = 3
      else:
        i += 2
  return out
​
​
def is_powerful(n):
  primes = set(prime_factorization(n))
  return all(n%i**2 == 0 for i in primes)

