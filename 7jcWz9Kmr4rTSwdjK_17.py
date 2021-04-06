
def prime_factorize(num):
  i = 2
  p = []
  while num > 1:
    if num%i == 0:
      p.append(i)
      num //= i
    else:
      i += 1
  return p

