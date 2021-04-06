
def possible_path(lst):
  return all(type(a) != type(b) for a, b in zip(lst, lst[1:]))

