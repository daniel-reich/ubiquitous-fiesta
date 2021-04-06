
def larger_than_right(lst):
  y = max(lst)
  g = lst.index(y)
  newlist = lst[g:]
  newerList = []
  for i,v in enumerate(newlist[:-1]):
    if v > max(newlist[i+1:]):
      newerList.append(v)
  
  if len(newlist) > 1:
    if newlist[-2] > newlist[-1]:
      newerList.append(newlist[-1])
  
  if len(newerList) == 0:
    newerList.append(y)
  
  return newerList

