
def is_it_inside(folders, x, y):
  if x in folders.get(y, []) or x == y:
    return True
  else:
    return any([is_it_inside(folders, x, i) for i in folders.get(y, [])])

