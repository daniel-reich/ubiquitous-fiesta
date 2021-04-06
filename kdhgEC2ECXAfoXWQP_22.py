
def transpose_matrix(mtx):
  mem = []
  for i in range(len(mtx[0])):
    for j in range(len(mtx)):
      mem += [mtx[j][i]]
  return ' '.join(mem)

