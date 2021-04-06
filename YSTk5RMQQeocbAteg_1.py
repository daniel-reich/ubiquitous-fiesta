
def tetra(n):
  x = []
  y = []
  for i in range(n + 1):
    x.append(i) 
    y.append(sum(x))
  return sum(y)

