
def move_to_end(lst, el):
  for x in range(lst.count(el)):
    lst.remove(el)
    lst.append(el)
  return lst

