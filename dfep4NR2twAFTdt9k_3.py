
def matrix_mult(m1, m2):
  m = [[0,0],[0,0]]
  m2 = list(zip(*m2))
  for i in range(2):
    for j in range(2):
      m[i][j] = sum(a*b for a,b in zip(m1[i],m2[j]))
  return m

