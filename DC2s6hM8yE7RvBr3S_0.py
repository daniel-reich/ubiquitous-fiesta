
def subtract_matrix(A, B):
  return [
    [float(i) - float(j) for i, j in zip(a, b)] 
    for a, b in zip(A, B)
  ]

