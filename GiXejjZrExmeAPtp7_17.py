
def fifth(*args):
  try:
    return type(args[4])
  except IndexError:
    return "Not enough arguments"

