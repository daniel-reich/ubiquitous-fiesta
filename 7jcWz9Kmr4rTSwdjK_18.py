
def prime_factorize(num):
  factor = 2
  res = []
  while num > 1:
    if num % factor == 0:
      res.append(factor)
      num = num // factor
    else:
      factor = factor + 1
  return res

