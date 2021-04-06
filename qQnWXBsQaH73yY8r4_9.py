
def kempner(n):
  for i in range(1, n+1):
    fac = 1
    for j in range(1, i+1):
      fac *= j
    if fac%n == 0:
      return i

