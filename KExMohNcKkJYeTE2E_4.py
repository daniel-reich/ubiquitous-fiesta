
def is_orthogonal(first, second):
  return sum(first[i]*second[i] for i in range(len(first)))==0

