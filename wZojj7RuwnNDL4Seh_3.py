
def completely_filled(lst):
  return all(x == '#' or x == '*' for b in lst for x in b)

