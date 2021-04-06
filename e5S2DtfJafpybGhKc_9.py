
def rotate(mat):
  return [[mat[i][j] for i in range(len(mat))][::-1] for j in range(len(mat))]

