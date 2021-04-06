
def find_it(items, name):
  if name in list(items):
    return "{} is gone...".format(name.capitalize())
  else:
    return "{} is here!".format(name.capitalize())

