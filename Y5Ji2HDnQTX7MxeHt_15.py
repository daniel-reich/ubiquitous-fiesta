
def snakefill(n):
  n = n * n
  i = 2
  a = []
  while True:
    if i > n:
      break
    a.append(i)
    i = i*2
​
  return len(a)

