
def add_it_up(lst):
  if type(lst[0]) == list:
    return sum(lst, [])
  elif type(lst[0]) == tuple:
    return sum(lst, ())
  else:
    return sum(lst)

