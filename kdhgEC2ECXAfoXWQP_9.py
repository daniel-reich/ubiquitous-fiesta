
def transpose_matrix(mtx):
  return ' '.join(m[x] for x in [i for i in range(len(mtx[0]))] for m in mtx)

