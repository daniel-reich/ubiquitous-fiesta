
def compare_data(*args):
  if len(args) == 0 or len(args) == 1:
    return True
  else:
    given_type = type(args[0])
    for eachelement in args:
      if type(eachelement) != given_type:
        return False
    return True

