
def multiply_matrix(m1, m2):
  if len(m1[0])!=len(m2):
    return "ERROR"
  return [[sum([m1[k][i]*m2[i][j] for i in range(len(m1[j]))]) for j in range(len(m1))] for k in range(len(m1))]

