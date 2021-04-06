
def move_to_end(lst, el):
  for i in lst:
    if i == el:
      lst.remove(i)
      lst.append(i)
  return lst

