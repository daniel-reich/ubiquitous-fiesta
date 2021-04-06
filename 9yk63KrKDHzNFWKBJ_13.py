
def is_it_inside(folders,X,Y):
  for i in folders.keys(): folders[i] += [i]
  for i in folders.keys():
    for j in folders.keys():
      if i in folders[j]: folders[j] += folders[i]
  if folders.get(Y) != None:
    if X in folders.get(Y): return True
  return False

