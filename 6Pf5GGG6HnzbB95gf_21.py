
def find_factors(n):
  if n < 1:
    return []
  res = []
  for i in range(1,int(n/2) + 1):
    if n % i == 0:
      res.append(i)
  res.append(n)
  return res

