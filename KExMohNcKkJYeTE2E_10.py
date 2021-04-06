
def is_orthogonal(first, second):
  dot_product = 0
  for i in range(len(first)):
    dot_product += first[i] * second[i]
  if dot_product == 0:
    return True
  else:
    return False

