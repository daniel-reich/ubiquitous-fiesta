
def is_orthogonal(first, second):
  k = 0
  i = 0
  while i < len(first):
    k += first[i] * second[i]
    i += 1
  if k == 0:
    return True
  else:
    return False

