
def nothing_is_nothing(*args):
  lst = []
  for i in args:
    lst.append(i)
  
  if all(lst):
    return True
  else:
    return False

