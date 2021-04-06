
def sort_it(lst):
  return sorted(lst, key=lambda x: x[0] if isinstance(x, list) else x)

