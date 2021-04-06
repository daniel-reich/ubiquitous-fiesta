
def transpose_matrix(mtx):
  return ' '.join(mtx[i][j] for j in range(len(mtx[0])) for i in range(len(mtx)))

