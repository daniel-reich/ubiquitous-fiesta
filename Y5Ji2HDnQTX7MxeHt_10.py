
def snakefill(n):
  x = 0
  y = 1
  while y*2 <= n*n:
    y *= 2
    x+=1
  return x

