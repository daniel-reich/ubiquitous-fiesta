
def prime_factorize(num):
  factors, i = [], 2
  while num > 1:
    if num % i == 0:
      num /= i
      factors.append(i)
    else:
      i += 1
  return sum([[i] * factors.count(i) for i in sorted(set(factors))], [])

