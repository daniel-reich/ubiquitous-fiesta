
def express_factors(n):
  i,res,chk,pf = 2,[],set(),[]
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      pf.append(i)
  if n > 1:
    pf.append(n)
  for s in pf:
    if s not in chk:
      pfcnt = pf.count(s)
      res.append('{}^{}'.format(s,pfcnt) if pfcnt > 1 else str(s))
      chk.add(s)
  return ' x '.join(res)

