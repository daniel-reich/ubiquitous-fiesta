
def is_it_inside(folders, X, Y):
  if X == Y:
    return True
​
  return False if Y not in folders else True if X in folders[Y] else any([is_it_inside(folders, X, i) for i in folders[Y]])

