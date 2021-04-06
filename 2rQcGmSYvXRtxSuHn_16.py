
def rotate_matrix(mat, turns=1):
  turns = turns%4
  new_mat = []
  if turns == 2:
    for i in mat[::-1]:
      new_mat.append(i[::-1])
  elif turns == 1:
    for i in mat[0]:
      new_mat.append([])
    for i in mat[::-1]:
      for j, k in enumerate(i):
        new_mat[j].append(k)
  elif turns == 3:
    for i in mat[0]:
      new_mat.append([])
    for i in mat:
      for j, k in enumerate(i[::-1]):
        new_mat[j].append(k)
  else:
    new_mat = mat[::]
  return new_mat

