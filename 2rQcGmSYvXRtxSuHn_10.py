
def rotate_matrix(mat, turns=1):
  if turns % 4 > 0:
    m, n = len(mat), len(mat[0])
    mat = [[mat[m-c_i-1][r_i] for c_i in range(m)] for r_i in range(n)]
    return rotate_matrix(mat, turns - 1)
  else:
    return mat

