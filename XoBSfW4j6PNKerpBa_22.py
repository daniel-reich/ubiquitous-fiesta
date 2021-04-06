
def complete_factorization(num):
  factors = []
  i = 2
  while num > 1:
    if num%i: i += 1
    else:
      num //= i
      factors.append(i)
  return factors

