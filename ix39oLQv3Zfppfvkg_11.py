
def multiply_matrix(m1, m2):
  n=len(m1)
  m=len(m2[0])
  M=[[0 for j in range(m)] for i in range(n)]
  m2_t=[list(x) for x in zip(*m2)]
  if len(m1[0])==len(m2):
    for i in range(n):
      for j in range(m):
        M[i][j]=sum(m1[i][k]*m2_t[j][k] for k in range(len(m1[0])))
    return M
  else:
    return "ERROR"

