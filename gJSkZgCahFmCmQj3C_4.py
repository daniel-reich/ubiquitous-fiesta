
def de_nest(lst):
  return lst[0] if type(lst[0]) != list else de_nest(lst[0])

