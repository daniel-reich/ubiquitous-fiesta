
def de_nest(lst):
  while isinstance(lst, list):
    lst = lst[0]
  return lst

