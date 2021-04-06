
def last_ancestor(folders, X, Y):
  X_ancestors = [X]
  Y_ancestors = [Y]
  not_top_level = []
  for lst in folders.values():
    for folder in lst:
      not_top_level.append(folder)
  for f in folders:
    if X in folders[f]:
      X_ancestors.append(f)    # closest ancestor of X
    if Y in folders[f]:
      Y_ancestors.append(f)    # closest ancestor of Y
  
  while X_ancestors[-1] in not_top_level:    # find all higher level ancestors of X
    for f in folders:
      if X_ancestors[-1] in folders[f]:
        X_ancestors.append(f)
  while Y_ancestors[-1] in not_top_level:    # find all higher level ancestors of Y
    for f in folders:
      if Y_ancestors[-1] in folders[f]:
        Y_ancestors.append(f)
  
  for folder in X_ancestors:
    if folder in Y_ancestors:
      return folder

