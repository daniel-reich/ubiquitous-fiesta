
def matrix_multiply(X, Y):
  if len(X[0])!=len(Y):return "invalid"
  return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

