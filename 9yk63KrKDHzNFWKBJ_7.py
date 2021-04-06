
def is_it_inside(folders, X, Y):
  if Y not in folders.keys():
    return False
  elif X == Y or X in folders[Y]:
    return True
  return any([is_it_inside(folders, X, y) for y in folders[Y]])

