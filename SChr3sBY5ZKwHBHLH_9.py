
def sort_it(l):
  return sorted(l, key = lambda x: x[0] if type(x) == list else x)

