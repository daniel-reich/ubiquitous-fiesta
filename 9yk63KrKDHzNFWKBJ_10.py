
def is_it_inside(folders, x, y):
  lst = [y]
  while lst:
    new_lst = []
    for i in lst:
      if i in folders.keys():
        for item in folders[i]:
          new_lst.append(item)
    lst = new_lst
    if x in lst: return True
  return x == y

