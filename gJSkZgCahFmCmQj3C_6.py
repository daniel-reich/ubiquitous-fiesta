
def de_nest(lst):
  if type(lst[0]) != list: return lst[0]
  return de_nest(lst[0])

