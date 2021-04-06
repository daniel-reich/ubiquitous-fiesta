
def de_nest(lst):
  while type(lst) is list:
    lst = lst[0]
  return lst

