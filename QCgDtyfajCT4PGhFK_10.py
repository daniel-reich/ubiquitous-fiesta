
def prime_factorization(number):
  n, factors = 2, []
  while number > 1:
    if number % n == 0:
      number //= n
      factors.append(n)
    else:
      n += 1
  return factors

