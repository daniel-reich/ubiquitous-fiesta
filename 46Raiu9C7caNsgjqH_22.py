
def compare_data(*args):
  result = True
  if len(args) == 0:
    return result
  else:
    item_type = type(args[0])
    for arg in args:
      if type(arg) != item_type:
        return False
  return result

