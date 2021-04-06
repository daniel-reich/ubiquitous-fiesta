
def move_to_end(lst, el):
  x=lst.count(el)
  while el in lst:
    lst.remove(el)
  lst.extend([el]*x)
  return lst

