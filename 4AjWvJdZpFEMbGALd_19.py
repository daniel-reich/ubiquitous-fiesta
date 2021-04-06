
def who_goes_free(n, k):
  p = list(range(n))
  x = k-1
  while len(p)>1:
    del p[x]
    x += k-1
    while x >= len(p):
      x = x-len(p)
  return p[0]

