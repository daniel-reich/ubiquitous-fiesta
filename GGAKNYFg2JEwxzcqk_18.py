
def anti_divisors(n):
  d = list()
  if n < 2: return d
  for i in range(1, n+1):
    if n % i and [not (n*2 % i), not ((n*2+1) % i)
      or not ((n*2-1) % i)][i & 1]: d += [i]
  return d

