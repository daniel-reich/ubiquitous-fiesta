
def anti_divisors(n):
  a = []
  for i in range (2, n):
    if n % i:
      if i % 2:
        if (n * 2 - 1) % i == 0 or (n * 2 + 1) % i == 0: a += [i]
      else:
        if (n * 2) % i == 0: a += [i]
  return a

