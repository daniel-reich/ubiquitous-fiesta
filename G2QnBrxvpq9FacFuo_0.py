
def possible_path(lst):
  return len(set(type(i) for i in lst[::2])) == 1

