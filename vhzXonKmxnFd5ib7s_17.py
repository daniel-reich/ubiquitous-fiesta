
def matrix_multiply(a, b):
  if len(a[0]) != len(b):
    return "invalid"
  return [[sum([x*y for (x,y) in zip(row,col)]) for col in zip(*b)] for row in a]

