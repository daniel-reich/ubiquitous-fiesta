
def junction_or_self(n):
  res = []
  for i in range(n,-1,-1):
    x = i
    tot = 0
    while x:
      x,r = divmod(x,10)
      tot += r
    if tot+i == n:
      res.append(i)
      if len(res) == 2:
        return res
  return res if res  else 'Self'

