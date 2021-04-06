
def transpose_matrix(mtx):
  return ' '.join([j[i] for i in range(len(mtx[0])) for j in mtx])

