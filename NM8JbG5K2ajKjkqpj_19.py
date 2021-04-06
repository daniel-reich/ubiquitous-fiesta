
def asc_des_none(lst, s):
  print(lst,s)
  new_list = []
  if s == 'None':
    return lst
  elif s == 'Asc':
    while lst:
      x = lst[0]
      for i in lst:
        if i < x:
          x = i
      new_list.append(x)
      lst.remove(x)
  elif s == 'Des':
    while lst:
      x = lst[0]
      for i in lst:
        if i > x:
          x = i
      new_list.append(x)
      lst.remove(x)
  print(lst)
  print(new_list)
  return new_list

