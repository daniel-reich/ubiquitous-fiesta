
def is_orthogonal(first, second):
  result = 0
  for i in range(len(first)):
    result = (first[i]*second[i]) + result
  if result == 0:
    return True
  else:
    return False

