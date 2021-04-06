
def rotate_matrix(*args):
  mat = args[0]
  turns = 1
  try:
    turns = args[1] % 4
  except IndexError:
    pass 
  mat_rot = [[mat[len(mat)-i-1][j] for i in range(0,len(mat))] for j in range(0,len(mat[0]))]
  return mat if turns == 0 else rotate_matrix(mat_rot,turns-1)

