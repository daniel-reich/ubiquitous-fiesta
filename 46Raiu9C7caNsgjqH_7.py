
def compare_data(*args):
  try:
    temp = type(args[0])
    for x in args:
      if type(x) != temp:
        return False
    return True
  except IndexError:
    return True

