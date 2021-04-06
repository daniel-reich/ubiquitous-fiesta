
def transpose_matrix(mtx):
  lst = []
  for x in range(len(mtx[0])):
    for y in range(len(mtx)):
      lst.append(mtx[y][x])
  return ' '.join(lst)

