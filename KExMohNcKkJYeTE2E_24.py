
def is_orthogonal(first, second):
  total = 0
  for i,j in zip(first, second):
    total = total + i * j
  return total == 0

