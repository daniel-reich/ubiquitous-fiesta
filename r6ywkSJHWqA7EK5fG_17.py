
def printgrid(x, y):
  return [
    [i + j for i in range(1, x * y + 1, x)] 
    for j in range(x)
  ]

