
def rotate_matrix(mat, turns=1):
  for _ in range(turns%4):
    mat = rot(mat)
  return mat
  
def rot(mat):
  return [list(z)[::-1] for z in zip(*mat)]

