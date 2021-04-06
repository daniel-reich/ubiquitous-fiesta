
def de_nest(lst):
  return de_nest(lst[0]) if type(lst) == list else lst

