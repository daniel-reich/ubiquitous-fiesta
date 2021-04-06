
def matrix_mult(m1, m2):
  n,k,m = len(m1), len(m1[0]), len(m2[0])
  return [[sum(m1[i][l]*m2[l][j] for l in range(k)) for j in range(m)] for i in range(n)]

