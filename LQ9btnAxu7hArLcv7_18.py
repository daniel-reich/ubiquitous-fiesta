
def diagonalize(n, d):
  res = [list(range(i, i+n)) for i in range(n)]
  if d in ("ur","lr"):
    res = [l[::-1] for l in res]
  if d in ("ll","lr"):
    res.reverse()
  return res

