
def find_it(items, name):
  return '{} is {}'.format(name.title(), 'gone...' if name in items else 'here!')

