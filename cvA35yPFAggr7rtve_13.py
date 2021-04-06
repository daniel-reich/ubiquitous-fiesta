
def parents(folders,lst):
  folder = lst[-1]
  for parent in folders:
    if folder in folders[parent]:
      lst.append(parent)
      return parents(folders,lst)
  return lst  
  
def last_ancestor(folders, X, Y):
  x_parents=parents(folders,list(X))
  y_parents=parents(folders,list(Y))
  for x_parent in x_parents:
    if x_parent in y_parents:
      return x_parent

