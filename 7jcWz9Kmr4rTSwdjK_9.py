
def prime_factorize(num):
  factors = []
  while num > 1:
    for x in range(2, num+1):
      if num % x == 0:
        factors.append(x)
        num //= x
        break
  return factors

