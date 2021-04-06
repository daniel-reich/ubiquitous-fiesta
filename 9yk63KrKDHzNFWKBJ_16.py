
def is_it_inside(folders, X, Y):
  if X == Y:
    return True
  try:
    if X in folders[Y]:
      return True
  except KeyError:
    return False
  else:
    return any(is_it_inside(folders, X, newY) for newY in folders[Y])

