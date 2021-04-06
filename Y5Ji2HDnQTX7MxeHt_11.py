
def snakefill(n):
  n*=n ; f = 1
  while (2**f) <= n:
    f+=1
  return f - 1

