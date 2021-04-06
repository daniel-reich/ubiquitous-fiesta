
def find_it(items, name):
  cap = name[0].upper() + name[1:]
  if name in items.keys():
    return cap + ' is gone...'
  else:
    return cap + ' is here!'

