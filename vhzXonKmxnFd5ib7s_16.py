
def matrix_multiply(a, b):
  if len(a[0])!= len(b): return "invalid"
  n, r, m = len(a), len(a[0]), len(b[0])
  return [[sum(a[i][k]*b[k][j] for k in range(r)) for j in range(m)] for i in range(n)]

