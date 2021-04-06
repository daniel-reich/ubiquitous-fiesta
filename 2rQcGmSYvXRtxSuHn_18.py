
def rotate_matrix(mat, turns=1):
  if turns==0:return mat
  if turns<0 or turns>3:return rotate_matrix(mat, turns%4)
  return rotate_matrix( [ [ y for y in x[::-1] ] for x in zip(*mat)]  , turns-1)

