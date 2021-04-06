
def possible_path(lst):
  return all(a == 'H' or b == 'H' for a, b in zip(lst[:-1], lst[1:]))

