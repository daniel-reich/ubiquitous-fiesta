
def get_last_ancestor(folders, f):
  for k,v in folders.items():
    if f in v:
      return k
  return None
​
def last_ancestor(folders,X,Y):
  if X == Y:
    return X
    
  x_ancestors = [X]
  while True:
    x_ancestor = get_last_ancestor(folders, x_ancestors[-1])
    if x_ancestor:
      if x_ancestor == Y: 
        return x_ancestor
      x_ancestors.append(x_ancestor)
    else:
      break
      
  y_ancestor = get_last_ancestor(folders, Y)
  while True:
    if y_ancestor in x_ancestors:
      return y_ancestor
    y_ancestor = get_last_ancestor(folders, y_ancestor)

