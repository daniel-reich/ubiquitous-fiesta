
def find_it(items, name):
  if name not in items.keys():
    return '{} is here!'.format(name.capitalize())
  else:
    return '{} is gone...'.format(name.capitalize())

