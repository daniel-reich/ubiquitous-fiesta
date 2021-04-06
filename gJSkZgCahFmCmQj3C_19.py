
def de_nest(lst):
  while type(lst) == list:
    lst = lst[0]
  return lst

