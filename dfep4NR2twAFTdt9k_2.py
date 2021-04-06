
def matrix_mult(m1, m2):
  return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m2)] for X_row in m1]

