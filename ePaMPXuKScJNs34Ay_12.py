
def add_it_up(lst):
  if isinstance(lst[0],list):
    return sum(lst,[])
  elif isinstance(lst[0],tuple):
    return sum(lst,())
  return sum(lst)

