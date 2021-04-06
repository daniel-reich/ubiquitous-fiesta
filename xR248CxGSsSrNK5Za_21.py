
def make_rug(m, n, s='#'):
  res = []
  for i in range(0,m):
    row = [s for i in range(0,n)]
    res.append("".join(row))
  return res

