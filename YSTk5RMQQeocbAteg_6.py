
def tetra(n):
  if n == 1:
    return n 
  else:
    return tetra(n-1) + sum([x for x in range(1, n+1)])

