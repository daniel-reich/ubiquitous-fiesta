
def flip_list(lst):
  if lst:
    if type(lst[0]) == int:
      vert_list = []
      for i in range(0, len(lst)):
        vert_list.append(list([lst[i]]))
      return vert_list
    else:
      hor_list = []
      for l in lst:
        hor_list.append(l[0])
      return hor_list
  else:
    return []

