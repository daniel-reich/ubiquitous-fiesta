
def possible_path(lst):
  return all(type(i) != type(j) for i, j in zip(lst, lst[1:]))

