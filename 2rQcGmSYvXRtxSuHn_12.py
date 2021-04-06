
def rotate_matrix(mat, turns=1):
  def rotate90(m):
    return [list(i[::-1])for i in zip(*m)]
  
  
  for i in range(turns%4):
    mat=rotate90(mat)
  return mat

