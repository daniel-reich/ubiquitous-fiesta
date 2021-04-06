
def find_it(items, name):
  if items.get(name) == None:
    return '{} is here!'.format(name.capitalize())
  else:
    return '{} is gone...'.format(name.capitalize())

