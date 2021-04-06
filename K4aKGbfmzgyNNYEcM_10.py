
def is_shape_possible(n, angles):
  if n<2:
    return False
  for i in angles:
    if i>180:
      return False
  if(sum(angles)<360 and n!=3):
    return False
  return True

