
def rotate(mat):
  return [[mat[i][j] for i in range(len(mat) - 1, -1, -1)] for j in range(0, len(mat))]

