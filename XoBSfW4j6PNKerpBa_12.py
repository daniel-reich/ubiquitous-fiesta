
def complete_factorization(num):
  i = 2
  factors = []
  while i*i <= num:
    if num % i != 0:
      i += 1
    else:
      num //= i
      factors.append(i)
  if num > 1:
    factors.append(num)
  return factors

