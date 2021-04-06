
def transpose_matrix(mtx):
  result = ""
  for i in range(len(mtx[0])):
    for j in mtx:
      result += j[i]+" "
  return result[:-1]

