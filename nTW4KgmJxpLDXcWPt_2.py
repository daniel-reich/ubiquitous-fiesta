
def move_to_end(lst, el):
  for item in lst:
    if item == el:
      lst.remove(item)
      lst.append(item)
  return lst

