
def move_to_end(lst, el):
  for x in lst:
    if x == el:
      lst.remove(el)
      lst.append(el)
  return lst

