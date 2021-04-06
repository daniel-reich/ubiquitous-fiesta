
def is_shape_possible(n, angles):
  if n<3:
    return False
  for a in angles:
    if a>180:
      return False
  if sum(angles)==(n-2)*180:
    return True
  else:
    return False

