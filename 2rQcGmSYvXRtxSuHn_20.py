
def rotate_matrix(mat, turns=1):
  turns = turns % 4
  if turns == 0:
    return mat
  else:
    n, m = (len(mat), len(mat[0])) if turns % 2 == 0 else (len(mat[0]), len(mat))
    return [[mat[m - c -1][r] if turns == 1 else mat[n - r - 1][m - c - 1] if turns == 2 else mat[c][n - r - 1] for c in range(m)] for r in range(n)]

