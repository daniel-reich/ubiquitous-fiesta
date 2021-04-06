
def transpose_matrix(mtx):
  lst = []
  for i in range(0, len(mtx[0])):
    for j in range(0, len(mtx)):
      lst.append(mtx[j][i])
  for i in range(0, len(lst)-1):
    lst[i] += " "
  return "".join(lst)

