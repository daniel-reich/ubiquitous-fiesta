
def find_it(items, name):
  if name.lower() in items:
    return '{} is gone...'.format(name.capitalize())
  else:
    return '{} is here!'.format(name.capitalize())

