
def last_ancestor(folders,X,Y):
  if X==Y:
    return X
  for i in folders:
    if (X in folders[i] or i==X) and (Y in folders[i] or i==Y):
      return i
  for i in folders:
    temp = []
    for j in folders[i]:
      if j in folders:
        temp+=folders[j]
    folders[i]+=temp
  return last_ancestor(folders,X,Y)

