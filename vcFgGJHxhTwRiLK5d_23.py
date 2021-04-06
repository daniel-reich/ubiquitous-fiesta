
def smallest(n):
  fact = []
  for i in range(2, n+1):
    if not any([i%f == 0 for f in fact]):
      power = i
      while power <= n:
        power *= i
        fact.append(i)
  prod = 1
  for f in fact:
    prod *= f
  return prod

