
def is_orthogonal(first, second):
  tot = 0
  for i in range(len(first)):
    tot = tot + (first[i]*second[i])
  return (tot == 0)

