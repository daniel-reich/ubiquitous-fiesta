
def tetra(n):
  number = 0
  for value in range(1, n+1):
    number += sum(range(1, value+1))
  return number

