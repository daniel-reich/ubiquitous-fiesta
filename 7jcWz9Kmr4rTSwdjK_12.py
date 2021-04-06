
def prime_factorize(num):
  i = 2
  res = []
  while i*i <= num:
    if num%i:
      i += 1
    else:
      res.append(i)
      num//=i
  if num > 1:
    res.append(num)
  return res

