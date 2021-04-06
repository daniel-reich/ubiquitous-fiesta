
def find_it(items, name):
  return '{} is gone...'.format(name.capitalize()) if name in items.keys() else '{} is here!'.format(name.capitalize())

