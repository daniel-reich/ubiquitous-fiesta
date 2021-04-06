
def incremental_depth(lst, tr = [], i = -1):
  if i == -1:
    tr = []
    tr.append(lst[i])
    i -= 1
    return incremental_depth(lst,tr,i)
  elif abs(i) == len(lst) + 1:
    return tr
  else:
    l = [lst[i]]
    l.append(tr)
    tr = l
    i -= 1
    return incremental_depth(lst,tr,i)

