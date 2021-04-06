
def babbage(n):
  l=len(str(n))
  for i in range(n):
    x=(i*10**l+n)**.5
    if x.is_integer():break
  if n==269696:return'Babbage was %scorrect!'%'in'*(x!=99736)
  return x

