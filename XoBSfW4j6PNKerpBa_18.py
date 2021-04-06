
def complete_factorization(n):
  d = 2
  ds = []
  while n > 1:
    if n % d == 0:
      n //= d
      ds.append(d)
      d = 2
    else:
      d += 1
  return ds

