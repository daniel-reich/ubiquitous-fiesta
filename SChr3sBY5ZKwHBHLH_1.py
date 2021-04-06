
def sort_it(lst):
  return sorted(lst, key=lambda x: x[0] if type(x) == list else x)

