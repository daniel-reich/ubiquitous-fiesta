
def is_it_inside(folders, X, Y):
  if Y == X:
    return True
  elif Y in folders.keys():
    if X in folders[Y]:
      return True
    else:
      for Y_bis in folders[Y]:
        return is_it_inside(folders, X, Y_bis)
  else: 
    return False

