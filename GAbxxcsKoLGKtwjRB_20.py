
def sum_primes(lst):
  x = []
  if lst:
    for i in lst:
      if i > 1:
        t = 0
        for y in range(1, i//2 + 1):
          if i % y == 0:
            t += 1
        if t <=1:
          x.append(i)
  else:
    return None
  return sum(x)

