
def find_it(items, name):
  return name.capitalize() + ' {}'.format(['is here!', 'is gone...'][name in items])

