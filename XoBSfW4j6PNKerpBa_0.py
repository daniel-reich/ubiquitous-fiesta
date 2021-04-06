
def complete_factorization(num):
  factors = []
  i = 2
  while i <= num:
    if not num % i:
      num /= i
      factors.append(i)
    else:
      i += 1
  return factors

