
def can_traverse(x):
  x = list(zip(*x))
  return all(abs(sum(x[i]) - sum(x[i-1])) < 2 for i in range(1, len(x)))

