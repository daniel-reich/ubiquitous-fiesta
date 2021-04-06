
def id_mtrx(n):
  if type(n) != int: return 'Error'
  m = abs(n)
  return [[1 if j == i else 0 for j in range(m)][::int(m/n)] for i in range(m)]

