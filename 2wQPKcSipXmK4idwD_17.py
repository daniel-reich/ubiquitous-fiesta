
def find_it(items, name):
  if items=={}:
    return "{} is here!".format(name.capitalize())
  elif name in list(items.keys()):
    return "{} is gone...".format(name.capitalize())
  else:
    return "{} is here!".format(name.capitalize())

