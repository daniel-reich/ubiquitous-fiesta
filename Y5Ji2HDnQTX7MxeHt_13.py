
def snakefill(n):
  num = 0
  length = 1
  while (n*n) >= (length*2):
    num += 1
    length *= 2 
  return num

