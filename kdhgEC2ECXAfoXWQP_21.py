
def transpose_matrix(mtx):
  res = ''
  for i in range(len(mtx[0])):
    for j in mtx:
      res += j[i] + ' '
​
  return res[:-1]

