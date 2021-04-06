
def prime_factors(num):
  a = []
  f = 2
  while num > 1:
    if num % f == 0:
      a.append(f)
      num /= f
    else:
      f += 1
  return a

