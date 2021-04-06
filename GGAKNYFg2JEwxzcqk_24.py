
def anti_divisors(n): 
  res = []
  for i in range(1, n):
    if n%i:
      if i%2 and (not ((n * 2) - 1)%i or not ((n * 2) + 1)%i):
        res.append(i)
      elif not i%2 and not (n*2)%i:
        res.append(i)
  return res

