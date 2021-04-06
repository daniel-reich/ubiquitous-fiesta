
def find_it(items, name):
  if name in items:
    return "{} is gone...".format(name.title())
  return "{} is here!".format(name.title())

