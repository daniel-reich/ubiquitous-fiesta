
def snakefill(n):
  len = 1
  i = 0
  while len <= n * n:
    len = len * 2
    i += 1
  return i - 1

