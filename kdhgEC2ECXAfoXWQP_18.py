
def transpose_matrix(mtx):
  return ' '.join(i[j] for j in range(len(mtx[0])) for i in mtx)

