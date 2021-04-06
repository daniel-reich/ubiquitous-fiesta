
def is_orthogonal(first, second):
  i = 0
  list = []
  for x in first:
    list.append(first[i]*second[i])
    i += 1
  return sum(list) == 0

