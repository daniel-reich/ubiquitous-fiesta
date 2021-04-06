
def is_it_inside(folders,X,Y):
  if X==Y:return True
  for i in folders:
    if X in folders[i]:return is_it_inside(folders,i,Y)
  return False

