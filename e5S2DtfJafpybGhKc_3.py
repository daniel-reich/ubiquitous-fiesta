
def rotate(mat):
  new_mat = []
  for i in range(len(mat[0])):
    li = list(map(lambda x: x[i], mat))
    li.reverse()
    new_mat.append(li)
  
  return new_mat

