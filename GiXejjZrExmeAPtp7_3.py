
def fifth(*args):
  if len(args) >= 5:
    return type(args[4])
  else:
    return "Not enough arguments"

