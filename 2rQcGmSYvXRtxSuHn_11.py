
from numpy import rot90
def rotate_matrix(mat, turns=1):
  return rot90(mat,turns+2).tolist() if turns%2 else rot90(mat,turns).tolist()

