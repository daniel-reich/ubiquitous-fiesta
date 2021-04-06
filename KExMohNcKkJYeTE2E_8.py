
def is_orthogonal(first, second):
  check = 0
  for index, value in enumerate(first):
    check+=(first[index]*second[index])
  return check == 0

