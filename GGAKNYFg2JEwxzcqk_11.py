
def anti_divisors(n):
  res = []
  for i in range(2,n):
    if n%i:
      if i%2:
        if not((n*2-1)%i and (n*2+1)%i):
          res.append(i)
      else:
        if not(n*2%i):
          res.append(i)
  return res

