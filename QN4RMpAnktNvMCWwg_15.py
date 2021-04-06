
def id_mtrx(n):
  if not isinstance(n, int):
    return "Error"
  elif n == 0:
    return []
  else:
    L = [[0]*abs(n) for x in range(abs(n))]
    for l in range(0, abs(n)):
      L[l][l] = 1
    if n < 0: L.reverse()
    return L

