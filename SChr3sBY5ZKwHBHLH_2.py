
def sort_it(lst):
  return sorted(lst, key=lambda x: x if type(x) is int else x[0])

