
def complete_factorization(num):
  i, factors = 2, []
  while num > 1:
    if num % i == 0:
      factors.append(i)
      num //= i
    else:
      i += 1
​
  return factors

