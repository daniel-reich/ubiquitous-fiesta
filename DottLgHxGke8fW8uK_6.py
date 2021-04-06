
def nPr(n, r):
  perm, lim = 1, n - r
  while n > lim:
    perm *= n
    n -= 1
  return perm
  
def nCr(n, r):
  if n - r < r:
    r = n - r
  fr, i = 1, r
  while i > 1:
    fr *= i
    i -= 1
  return nPr(n, r) // fr

