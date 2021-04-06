
def multiply_matrix(m1, m2):
  if len(m1)!=len(m2[0]) or len(m1)!=len(m2[0]):
    return 'ERROR'
  final = [[0 for i in range(len(m1))] for j in range(len(m2[0]))]
  for i in range(len(m1)):
    for j in range(len(m2[0])):
      for k in range(len(m2)):
        final[i][j] += m1[i][k]*m2[k][j]
  return final

