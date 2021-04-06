
def matrix_multiply(m, n):
  try:
    return [[sum(m[i][j] * n[j][k] for j in range(len(n))) for k in range(len(n[0]))] for i in range(len(m))]
  except IndexError:
    return "invalid"

