
def prime_factors(num):
  factors = []
  fac = 2
  while num > 1:
    if num%fac == 0:
      factors.append(fac)
      num /= fac
    else:
      fac += 1
  return factors

