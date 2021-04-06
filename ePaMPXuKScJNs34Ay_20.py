
def add_it_up(lst):
  if type(lst[0]) == int or type(lst[0]) == float:
    return sum(lst)
  else:
    if isinstance(lst[0], list) == True:
      return sum(lst, [])
    else:
      return sum(lst, ())

