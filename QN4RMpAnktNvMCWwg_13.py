
def id_mtrx(n):
  if not isinstance(n, int): 
    return 'Error'
  nn = abs(n)
  m = [[0 for i in range(nn)] for j in range(nn)] 
  if n > 0:
    for i in range(nn): 
      m[i][i] = 1
  if n < 0:
    for i in range(nn):
      m[i][-i-n-1] = 1
  return m

