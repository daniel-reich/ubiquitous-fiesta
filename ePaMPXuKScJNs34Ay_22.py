
def add_it_up(lst):
  if type(lst[0]) is list:
    return sum(lst,[])
  elif type(lst[0]) is tuple:
    return sum(lst,())
  else:
    return sum(lst)

