
def is_orthogonal(first, second):
  return not bool(sum([i*second[j] for j,i in enumerate(first)]))

