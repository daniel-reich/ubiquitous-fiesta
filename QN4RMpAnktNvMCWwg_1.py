
def id_mtrx(n):
  try:
    n, rev = abs(n), -1 if n<0 else 1
    return [[int(i==j) for j in range(n)][::rev] for i in range(n)]
  except: return "Error"

