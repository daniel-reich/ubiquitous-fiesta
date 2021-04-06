
def find_it(items, name):
  N = name.capitalize()
  return N + ' is gone...' if name in items else N + ' is here!'

