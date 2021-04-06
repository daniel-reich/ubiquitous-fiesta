
def incremental_depth(lst):
  while len(lst) > 1:
    tmp = lst.pop()
    if type(tmp) != list: tmp = [tmp]
    tmp2 = lst.pop()
    lst.append([tmp2])
    lst[-1].append(tmp)
  lst = lst[0]
  return lst

