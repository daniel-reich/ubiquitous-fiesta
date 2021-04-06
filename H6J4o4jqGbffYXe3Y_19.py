
def relation_lst(lst):
  newlist = []
  if len(lst) == 0:
    return []
  elif len(lst) == 1:
    return [(lst[0],lst[0])]
  else:
    x = sorted(lst)
    for i in range(len(x)):
      newlist.append((x[i],x[i]))
      y = x[i+1:]
      for a in range(len(y)):
        newlist.append((x[i],y[a]))
    return newlist

