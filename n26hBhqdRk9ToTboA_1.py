
def nothing_is_nothing(*args):
  none_bool = True
  for arg in args:
    if arg == False or arg == None:
      none_bool = False
      break
    else:
      continue
  return none_bool

