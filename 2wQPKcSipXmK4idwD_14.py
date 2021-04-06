
def find_it(items, name):
  print(items,name)
  if name in items.keys():
    return '{} is gone...'.format(name.capitalize())
  else:
    return '{} is here!'.format(name.capitalize())

