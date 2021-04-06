
def is_orthogonal(first, second):
  return not sum( f*s for f,s in zip(first,second))

