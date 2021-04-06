
def fifth(*args):
  try:
    return type(args[4])
  except:
    return 'Not enough arguments'

