
def snakefill(n):
  length=1
  res = 0
  while(length <= n*n):
    length = length * 2
    res += 1
  return res-1

