
def is_it_inside(folders,X,Y):
  if Y not in folders:
    return False
  if X==Y or X in folders[Y]:
    return True
  return any(is_it_inside(folders,X,child) for child in folders[Y])

