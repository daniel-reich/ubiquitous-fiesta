
def de_nest(lst):
  i = lst
  while type(i) == list:
    i = i[0]
  return i

