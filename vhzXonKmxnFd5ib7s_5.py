
def matrix_multiply(M, N):
  if len(M[0]) != len(N):
    return 'invalid'
  return [[sum(i*j for i, j in zip(m, n)) for n in zip(*N)] for m in M]

