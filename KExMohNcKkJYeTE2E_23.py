
def is_orthogonal(x1, x2):
  return sum([i*n for i,n in list(zip(x1, x2))]) == 0

