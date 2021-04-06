
def is_it_inside(folders,X,Y):
  if X==Y or (Y in folders and X in folders[Y]):
    return True
  if any([X in folders[i] for i in folders]):
    return is_it_inside(folders,[i for i in folders if X in folders[i]][0],Y)
  return False

