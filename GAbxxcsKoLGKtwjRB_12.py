
def sum_primes(lst):
  res = 0
  for x in lst:
    if (x == 2):
      res = res + 2
    for a in range (2, x):
      if (x % a == 0):
        break
      if (a == x - 1):
        res = res + x
  if (res == 0):
    return None
  return res

