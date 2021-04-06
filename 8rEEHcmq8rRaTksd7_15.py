
def lines_are_parallel(l1, l2):
  Gradient1 = - l1[0] / l1[1]
  Gradient2 = - l2[0] / l2[1]
  if Gradient1 == Gradient2:
    return True
  else:
    return False

