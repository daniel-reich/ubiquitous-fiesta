
def prime_factors(num):
  res, i = [], 2
  while num != 1:
    while not num%i:
      res.append(i)
      num //= i
    i += 1
  return res

