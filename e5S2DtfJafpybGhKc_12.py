
def rotate(mat):
  n = len(mat)
  return [[mat[n-1-r][c] for r in range(n)] for c in range(n)]

