
def transpose_matrix(mtx):
  return " ".join([bar[foo] for foo in range(len(mtx[0])) for bar in mtx])

