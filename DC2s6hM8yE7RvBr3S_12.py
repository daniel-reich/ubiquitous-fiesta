
def subtract_matrix(A, B):
  return [[float(a)-float(b) for a, b in zip(row_A, row_B)] for row_A, row_B in zip(A, B)]

